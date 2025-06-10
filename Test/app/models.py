from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class CustomUser(AbstractUser):
    is_user =models.BooleanField(default=False)

class TaskUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='u')
    name = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)

class Tasks(models.Model):
    user = models.ForeignKey(TaskUser,on_delete=models.CASCADE,related_name='task_users')
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)



