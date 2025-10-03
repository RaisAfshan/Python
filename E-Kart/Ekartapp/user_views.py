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

@login_required(login_url='login1')
def product_detail(request):
    return render(request,'user/productView/productDetail.html')

def all_products(request):
    return render(request,'user/products/allproducts.html')

def category_product(request):
    return render(request,'user/category/categoryProduct.html')

def sub_category_product(request):
    return render(request,'user/category/subcategory.html')



