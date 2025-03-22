from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


from vaccine_app.form import CustomUser_reg, User_reg, Nurse_reg


# Create your views here.
#HOME
def home(request):
    return render(request,'index.html')


@login_required(login_url='sigin_in1')
def admin_dasboard(request):
    return render(request,'dashboard.html')

#User registration
def user_login(request):
    user_log_form = CustomUser_reg()
    user_form = User_reg()
    if request.method =='POST':
        user_log_form=CustomUser_reg(request.POST)
        user_form = User_reg(request.POST)
        if user_log_form.is_valid() and user_form.is_valid():
            ulogin = user_log_form.save(commit=False)
            ulogin.is_user = True
            ulogin.save()

            users = user_form.save(commit=False)
            users.user = ulogin
            users.save()
            return redirect('sigin_in1')
    return render(request,'user_reg.html',{'user_log_form':user_log_form,'user_form':user_form})

#Nurse registration
def nurse_login(request):
    nurse_log_form = CustomUser_reg()
    nurse_form = Nurse_reg()
    if request.method == 'POST':
        nurse_log_form = CustomUser_reg(request.POST)
        nurse_form = Nurse_reg(request.POST)
        if nurse_log_form.is_valid() and nurse_form.is_valid():
            nlogin = nurse_log_form.save(commit=False)
            nlogin.is_nurse = True
            nlogin.save()

            nurse = nurse_form.save(commit=False)
            nurse.user = nlogin
            nurse.save()
            return redirect('sigin_in1')
    return render(request,'nurse_register.html',{'nurse_log_form':nurse_log_form,'nurse_form':nurse_form})

def Sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('dash_home1')
            if user.is_nurse:
                return redirect('nurse_dash1')
            if user.is_user:
                return redirect('userdash1')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login1.html')

def logout_view(request):
    logout(request)
    return redirect('sigin_in1')

def register(request):
    return render(request,'sign_up.html')

@login_required(login_url='sigin_in1')
def dash_home(request):
    return render(request,'dash_home.html')




