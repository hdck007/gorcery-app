from django.urls import path
from .views import (
  ProductListView,
  ProductDetailView,
  ProductCreateView,
  ProductUpdateView,
  ProductDeleteView,
  UserProductListView,
)
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserProductListView.as_view(), name='user-products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/new/', ProductCreateView.as_view(), name='post-create'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search, name='search'),
    path('order/', views.order, name='order')
]