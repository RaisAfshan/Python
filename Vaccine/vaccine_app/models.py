from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Hospital(models.Model):
    name=models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=100)
    vaccine_type = models.CharField(max_length=100)
    description = models.TextField()
    # vaccine_update

    def __str__(self):
        return self.vaccine_name

class CustomUser(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

class Nurse(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=100)
    contact_no =models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    hospital = models.ForeignKey(Hospital,on_delete=models.DO_NOTHING)

class User(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    child_age = models.CharField(max_length=100)
    # child gender
    recent_vaccination = models.TextField(null=True,blank=True)

class Complaints(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,null=True,blank=True)
    subject = models.CharField(max_length=200)
    complaint = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True,blank=True)

class Vaccineshedule(models.Model):
    hospital_name = models.ForeignKey(Hospital,on_delete=models.DO_NOTHING,null=True,blank=True)
    vaccine = models.ForeignKey(Vaccine,on_delete=models.DO_NOTHING,null=True,blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Vaccine_Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='appointment',null=True,blank=True)
    schedule = models.ForeignKey(Vaccineshedule,on_delete=models.CASCADE,null=True,blank=True )
    status = models.IntegerField(default=0)
    vaccine_name = models.ForeignKey(Vaccine,on_delete=models.DO_NOTHING, null=True,blank=True)








