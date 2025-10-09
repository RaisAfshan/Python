from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from Ekartapp.form import userAddressForm
from Ekartapp.models import Product, Category, ProductVariant, ProductVariantImage, Custom_User, UserModel, UserAddress
from django.shortcuts import render, get_object_or_404

def user_home(request):
    return render(request,'user/userHome.html')


def user_productHome(request):
    basePrice = ProductVariant.objects.filter(price__lte=80000,product__category__name='Smartphones')[:4]
    # category = ProductVariant.objects.
    context = {
        'basePrice': basePrice
    }
    return render(request,'user/userProductHome.html',context)

@login_required(login_url='login1')
def user_cart(request):
    # cart_item = get_object_or_404(ProductVariant,id=id)
    # print(cart_item)
    # quantity = ProductVariant.objects.filter(id=cart_item)
    return render(request,'user/cart/userCart.html')






def product_detail(request, id):
    product_variant = get_object_or_404(ProductVariant, id=id)
    product = product_variant.product

    primary_values = ProductVariant.objects.filter(
        product=product
    ).values_list('primary_variant__value', flat=True).distinct()

    selected_primary = request.GET.get('primary', product_variant.primary_variant.value)
    selected_secondary = request.GET.get('secondary', None)

    filtered_variants = ProductVariant.objects.filter(
        product=product,
        primary_variant__value=selected_primary
    )

    secondary_values = filtered_variants.values_list('secondary_variant__value', flat=True).distinct()

    if selected_secondary:
        current_variant = filtered_variants.filter(secondary_variant__value=selected_secondary).first()
    else:
        current_variant = filtered_variants.first()

    context = {
        'prodDetail': current_variant or product_variant,
        'primary_values': primary_values,
        'secondary_values': secondary_values,
        'selected_primary': selected_primary,
        'selected_secondary': selected_secondary,
    }

    return render(request, 'user/productView/productDetail.html', context)


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
    user = UserModel.objects.filter(user=request.user).first()
    address = UserAddress.objects.filter(user=user).first()
    return render(request,'user/userProfile/user_Profile.html',{'user':user,'address':address})

# Address CRUD
@login_required(login_url='login1')
def user_address(request):
    u = UserModel.objects.get(user=request.user)
    address = UserAddress.objects.filter(status=True , user=u)
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

@login_required(login_url='login1')
def updateAddress(request,id):
    edit_address = UserAddress.objects.get(id=id)
    if request.method== 'POST':
       editForm = userAddressForm(request.POST,instance=edit_address)
       if editForm.is_valid():
           editForm.save()
           return redirect('userAddress')
    else:
        editForm = userAddressForm(instance=edit_address)
    return render(request,'user/userProfile/editAddress.html',{'editForm':editForm})

@login_required(login_url='login1')
def deleteAddress(request,id):
    delete_address = UserAddress.objects.get(id=id)
    delete_address.status = False
    delete_address.save()
    return redirect('userAddress')










