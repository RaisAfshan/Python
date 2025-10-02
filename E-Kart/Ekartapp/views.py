from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect

from Ekartapp.form import CustomUserForm, UserForm


# Create your views here.

def index(request):
    return render(request,'index.html')

def userRegisteration(request):
    customReg = CustomUserForm()
    userReg = UserForm()

    if request.method == 'POST':
        customReg = CustomUserForm(request.POST)
        userReg = UserForm(request.POST,request.FILES)
        if customReg.is_valid() and userReg.is_valid():
            cReg = customReg.save(commit=False)
            cReg.is_user = True
            cReg.save()
            uReg = userReg.save(commit=False)
            uReg.user = cReg
            uReg.save()
            return redirect('login1')
    return render(request,'userRegister.html',{'customReg':customReg,'userReg':userReg})

def loginUser(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    user =authenticate(request, username=username,password=password)
    if user is not None:
        login(request,user)
        if user.is_staff:
            return redirect('adminHomePage')
        if user.is_user:
            return redirect('userProductHome')
        else:
            messages.info(request,"Invalid Credentials")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

