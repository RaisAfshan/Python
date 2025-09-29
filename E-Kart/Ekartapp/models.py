from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextField

from Ekartapp.Choices import GENDER_CHOICES, ADDRESS_TYPE_CHOICES


# Create your models here.

class Custom_User(AbstractUser):
    is_user =models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserModel(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,related_name='User')
    fullName = models.CharField(max_length=500)
    phoneNumber = models.CharField(max_length=20,unique=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES, default='Male')
    profilePicture = models.FileField(upload_to='upload/')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserAddress(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='address')
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES,default='HOME')
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default='India')
    zip_code = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

class Category(models.Model):
    name= models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='subcategory', null=True,blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    created_by = models.ForeignKey(Custom_User,on_delete=models.CASCADE,related_name='product')
    title=models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=False) #True
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category_products")
    # created_at


# class ProductVariant(models.Model):
#     attribute = models.CharField(max_length=200,blank=True,null=True)
#     value = models.ForeignKey('self',on_delete=models.CASCADE,related_name='product_variants')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_var')
#
#
# class ProductImage(models.Model):
#     product_image = models.ImageField(upload_to='upload/')
#     alt_text=models.CharField(max_length=100)
#     is_primary = models.BooleanField(default=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_image')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering= ['-is_primary','created_at']
















