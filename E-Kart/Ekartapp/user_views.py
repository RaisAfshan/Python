from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login1')
def user_home(request):
    return render(request,'user/userHome.html')

@login_required(login_url='login1')
def user_productHome(request):
    return render(request,'user/userProductHome.html')

@login_required(login_url='login1')
def user_cart(request):
    return render(request,'user/cart/userCart.html')



