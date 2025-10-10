from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextField
from django.utils import timezone
from Ekartapp.Choices import GENDER_CHOICES, ADDRESS_TYPE_CHOICES, ORDER_STATUS
from decimal import Decimal


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
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.fullName

class UserAddress(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='address')
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES,default='HOME')
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default='India')
    zip_code = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Category(models.Model):
    name= models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='subcategory', null=True,blank=True) # Parent = Null : then its main category
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class VariantType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Variants(models.Model):
    variant_type = models.ForeignKey(VariantType,on_delete=models.CASCADE,related_name='variant_type')
    value = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.variant_type.name} - {self.value}"


class Product(models.Model):
    created_by = models.ForeignKey(Custom_User,on_delete=models.CASCADE,related_name='product')
    brand = models.CharField(max_length=300, null=True)
    title=models.CharField(max_length=300)
    description = models.TextField()
    primary_variant = models.ForeignKey(VariantType,on_delete=models.CASCADE,related_name='primary_variant_type')
    secondary_variant = models.ForeignKey(VariantType,on_delete=models.CASCADE,related_name='secondary_variant_type',null=True,blank=True)
    status=models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category_products")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_variant')
    primary_variant = models.ForeignKey(Variants,on_delete=models.CASCADE,related_name='primary_product_variant')
    secondary_variant = models.ForeignKey(Variants,on_delete=models.CASCADE,related_name='secondary_product_variant',null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    is_default = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if self.is_default:
            ProductVariant.objects.filter(product=self.product,is_default = True).update(is_default=False )
        super().save(*args,**kwargs)

    def get_default_image(self):
        return self.images.filter(is_default=True).first()

    def __str__(self):
        if self.secondary_variant:
            return f"{self.product.title} - {self.primary_variant.value}/{self.secondary_variant.value}"
        return f"{self.product.title} - {self.primary_variant.value}"

class ProductVariantImage(models.Model):
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='product')
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_variant} - Image"

class Coupons(models.Model):
    code = models.CharField(max_length=50)
    discount_amount = models.DecimalField(max_digits=10,decimal_places=2)
    discount_percent = models.PositiveIntegerField(null=True,blank=True)
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    def is_valid(self):
        return self.is_active and self.expiry_date >= timezone.now()

class Cart(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE, related_name="cart" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coupons = models.ForeignKey(Coupons,null=True,blank=True,on_delete=models.SET_NULL)

    @property
    def total_price(self):
        subtotal = sum(item.total_price for item in self.items.all())
        gst = subtotal * Decimal('0.18')
        delivery = Decimal('40.0')
        discount = Decimal(0.00)

        if self.coupons and self.coupons.is_valid():
            if self.coupons.discount_amount:
                discount = Decimal(self.coupons.discount_amount)
            elif self.coupons.discount_percent:
                discount = subtotal * Decimal(self.coupons.discount_percent) / Decimal(100)
        return subtotal + gst + delivery - discount

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product_variant.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user_order')
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    address = models.ForeignKey('UserAddress', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20,choices=ORDER_STATUS,default='Order Placed')
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,related_name='prod_order')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def get_subtotal(self):
        return self.quantity * self.price

class CarouselImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='carousel/')
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
























