from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( 
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
) 
from .models import Product
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


class ProductListView(ListView):
  model = Product
  context_object_name = 'products'
  ordering = ['-date_posted']
  template_name = 'store/home.html'  #<app>/<model>_<viewtype>.html
  paginate_by = 3

class UserProductListView(ListView):
  model = Product
  context_object_name = 'products'
  template_name = 'store/user_products.html'  #<app>/<model>_<viewtype>.html
  paginate_by = 5
  
  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Product.objects.filter(shop=user).order_by('-date_posted')
    
  
class ProductDetailView(DetailView):
  model = Product
  
class ProductCreateView(SuccessMessageMixin ,LoginRequiredMixin, CreateView):
  model = Product
  success_message = "Your product is Created!"
  fields = ['name', 'description', 'price', 'quantity', 'image']
  
  
  def form_valid(self, form):
    form.instance.shop = self.request.user
    return super().form_valid(form)

class ProductUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
  model = Product
  fields = ['name', 'description', 'price','quantity', 'image']
  success_message = "Your product is Updated!"
  
  def form_valid(self, form):
    form.instance.shop = self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    product = self.get_object()
    if self.request.user == product.shop:
      return True
    return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
  model = Product
  def test_func(self):
    product = self.get_object()
    if self.request.user == product.shop:
      return True
    return False
  success_url = '/'  
    
def about(request):
  return render(request, 'store/about.html')
  
def home(request):
  return render(request, 'store/startpage.html')

def search(request):
  query = request.GET['query']
  products = Product.objects.filter(name__icontains=query)
  params = {'products': products,
            'query': query}
  return render(request, 'store/search.html', params)

@login_required
def order(request):
  quantity = request.GET['quantity']
  address = request.GET['address']
  product_id = request.GET['id']
  product = get_object_or_404(Product, pk=product_id)
  if (int(quantity)<=product.quantity and int(quantity) > 0):
    user = request.user
    amount = int(quantity)*product.price 
    email_subject = 'Order Reciept'
    message = render_to_string('store/reciept.html', {
              'user': user,
              'quantity' : quantity,
              'amount' : amount,
              'product' : product
          })
    to_email = request.user.email
    email = EmailMessage(email_subject, message, to=[to_email])
    email.send()
    messageForShop = render_to_string('store/shopreciept.html', {
              'user': user,
              'quantity' : quantity,
              'address': address,
              'amount' : amount,
              'product' : product
          })
    to_email_shop = product.shop.email
    emailShop = EmailMessage(email_subject, messageForShop, to=[to_email_shop])
    emailShop.send()
    product.quantity = product.quantity - int(quantity)
    product.save()
    return render(request, 'store/order.html')
  else:
    return HttpResponse('The quantity you ordered is invalid')