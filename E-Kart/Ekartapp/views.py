from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect

from Ekartapp.form import CustomUserForm, UserForm
from Ekartapp.models import Custom_User, EmailOTP
from Ekartapp.utility import send_otp


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
            cReg.is_active = False
            cReg.set_password(customReg.cleaned_data['password1'])
            cReg.save()

            uReg = userReg.save(commit=False)
            uReg.user = cReg
            uReg.save()

            send_otp(cReg)

            request.session['user_id'] = cReg.id
            return redirect('verify_otp')


    return render(request,'userRegister.html',{'customReg':customReg,'userReg':userReg})

def verify_otp_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('Register1')

    user = Custom_User.objects.get(id=user_id)
    otp_record = EmailOTP.objects.filter(user=user).first()

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')

        if otp_record and otp_record.otp == entered_otp:
            if otp_record.is_expired():
                error = "OTP expired. Please register/login again."
            else:
                user.is_active = True
                user.save()
                otp_record.is_verified = True
                otp_record.save()
                messages.success(request, "OTP verified successfully!")
                return redirect('login1')
        else:
            error = 'Invalid OTP'
        return render(request,'verify_otp.html',{'error':error})
    return render(request,'verify_otp.html')



def loginUser(request):
    if request.user.is_authenticated:
        if request.user.is_user:
            return redirect('userProductHome')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        try:
            user_obj = Custom_User.objects.get(username=username)
        except Custom_User.DoesNotExist:
            user_obj = None

        if user_obj and not user_obj.is_active:
            send_otp(user_obj)
            messages.warning(request,'Please verify your email before logging in.')
            request.session['user_id'] = user_obj.id
            return redirect('verify_otp')

        user =authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            next_url = request.GET.get('next') or request.GET.get('next') or 'userProductHome'
            if next_url:
                return redirect(next_url)

            if user.is_staff:
                return redirect('adminHomePage')
            if user.is_user:
                return redirect('userProductHome')
        else:
            messages.info(request,"Invalid Credentials")

    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('userProductHome')



