from django.shortcuts import render

from Ekartapp.form import CustomUserForm


# Create your views here.

def index(request):
    return render(request,'index.html')


