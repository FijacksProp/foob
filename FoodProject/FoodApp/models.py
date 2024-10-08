from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
     name = models.OneToOneField(User, on_delete=models.CASCADE)
     phone = models.CharField(max_length=15)
     bio = models.CharField(max_length=100)
     pic = models.ImageField(upload_to='images/foodsite_img')

class Category(models.Model):
     name = models.CharField(max_length=15)
     img = models.ImageField(upload_to='images/foodsite_img', null=True, blank=True)
     description = models.CharField(max_length=30)

class Menu(models.Model):
    img = models.ImageField(upload_to='images/foodsite_img', null=True, blank=True)
    name = models.CharField(max_length=20, default='Enter a name')
    description = models.CharField(max_length=100, default='Describe your product')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)
    active_status = models.BooleanField()

