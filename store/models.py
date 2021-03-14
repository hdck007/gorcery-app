from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Product(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(default='write your description here',max_length=255)
  price = models.FloatField()
  date_posted = models.DateTimeField(default=timezone.now)
  shop = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='product_image/')
  quantity = models.IntegerField()
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    
    img = Image.open(self.image.path)
    
    if img.height > 300 or img.width > 300:
      output_size = (400 , 300)
      img.thumbnail(output_size)
      img.save(self.image.path)

      
  
  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('product-detail', kwargs={'pk': self.pk})