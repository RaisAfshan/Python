from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from Ekartapp.form import userAddressForm
from Ekartapp.models import Product, Category, ProductVariant, ProductVariantImage, Custom_User, UserModel, UserAddress


def user_home(request):
    return render(request,'user/userHome.html')


def user_productHome(request):
    return render(request,'user/userProductHome.html')

@login_required(login_url='login1')
def user_cart(request):
    return render(request,'user/cart/userCart.html')


# def product_detail(request,id):
#     product = ProductVariant.objects.get(id=id)
#     primary_values = ProductVariant.objects.filter(product=product.product).values_list('primary_variant__value',flat=True).distinct()
#     selected_primary = request.GET.get('primary',product.primary_variant.value)
#     filtered_variants = ProductVariant.objects.filter(product=product.product,primary_variant__value=selected_primary)
#
#     if product.secondary_variant:
#         secondary_values = filtered_variants.values_list('secondary_variant__value',flat=True).distinct()
#     else:
#         secondary_values=[]
#
#     context = {
#         'prodDetail': product,
#         'primary_values':primary_values,
#         'secondary_values':secondary_values,
#         'selected_primary':selected_primary
#     }
#     return render(request,'user/productView/productDetail.html',context)


def product_detail(request,id):
    product = ProductVariant.objects.get(id=id)
    primary_values = ProductVariant.objects.filter(product=product.product).values_list('primary_variant__value',flat=True).distinct()
    selected_primary = request.GET.get('primary',product.primary_variant.value)
    filtered_variants = ProductVariant.objects.filter(product=product.product,primary_variant__value=selected_primary)

    if product.secondary_variant:
        secondary_values = filtered_variants.values_list('secondary_variant__value',flat=True).distinct()
    else:
        secondary_values=[]

    context = {
        'prodDetail': product,
        'primary_values':primary_values,
        'secondary_values':secondary_values,
        'selected_primary':selected_primary
    }
    return render(request,'user/productView/productDetail.html',context)

# All products
def all_products(request):
    products = ProductVariant.objects.filter(is_default=True).prefetch_related('images')
    return render(request,'user/products/allproducts.html',{'products':products})

# Category
def category_product(request):
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
            products = ProductVariant.objects.filter(product__category__in=sub_category,is_default=True).prefetch_related('images')
        else:
            products = ProductVariant.objects.filter(product__category=category,is_default=True).prefetch_related('images')
    else:
        products = Product.objects.filter(category=category,is_default=True).prefetch_related('images')
    return render(request,'user/category/subcategory.html',{'current_category':category,'products':products,'category':categories})

@login_required(login_url='login1')
def user_profile(request):
    return render(request,'user/userProfile/user_Profile.html')

@login_required(login_url='login1')
def user_address(request):
    u = UserModel.objects.get(user=request.user)
    address = UserAddress.objects.filter(status=False , user=u)
    return render(request,'user/userProfile/userAddress.html',{'address':address})

@login_required(login_url='login1')
def user_postAddress(request):
    addressForm = userAddressForm()
    if request.method == 'POST':
        addressForm = userAddressForm(request.POST)
        if addressForm.is_valid():
            address = addressForm.save(commit=False)
            u = UserModel.objects.get(user=request.user)
            address.user = u
            address.save()
            messages.success(request,'address added successfully')
            return redirect('userAddress')
        else:
            messages.error(request, 'error adding address')
    return render(request,'user/userProfile/postAddress.html',{'addressForm':addressForm})








