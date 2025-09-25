from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models

from Ekartapp.Choices import GENDER_CHOICES


# Create your models here.

class Custom_User(AbstractUser):
    is_user =models.BooleanField(default=False)


class UserModel(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,related_name='User')
    fullName = models.CharField(max_length=500)
    phoneNumber = models.CharField(max_length=20,unique=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES, default='Male')
    profilePicture = models.FileField(upload_to='upload/')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)




