from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render

from Ekartapp.models import Product, Category



def user_home(request):
    return render(request,'user/userHome.html')


def user_productHome(request):
    return render(request,'user/userProductHome.html')

@login_required(login_url='login1')
def user_cart(request):
    return render(request,'user/cart/userCart.html')


def product_detail(request):
    return render(request,'user/productView/productDetail.html')

# All products
def all_products(request):
    products = Product.objects.filter(status=True)
    return render(request,'user/products/allproducts.html',{'products':products})

# Category
def category_product(request):
    # Only active parent categories
    categories = Category.objects.filter(status=True,parent__isnull=True)
    context = {
        'category': categories
    }
    return render(request, 'user/category/categoryProduct.html', context)

def sub_category_product(request,id):
    category = Category.objects.get(id=id)
    categories  = Category.objects.filter(status=True,parent__isnull=True)
    if category.parent is None:
        sub_category = category.subcategory.all()
        if sub_category.exists():
            products = Product.objects.filter(category__in=sub_category)
        else:
            products = Product.objects.filter(category=category)
    else:
        products = Product.objects.filter(category=category)
    return render(request,'user/category/subcategory.html',{'current_category':category,'products':products,'category':categories})

@login_required(login_url='login1')
def user_profile(request):
    return render(request,'user/userProfile/user_Profile.html')

@login_required(login_url='login1')
def user_address(request):
    return render(request,'user/userProfile/userAddress.html')






