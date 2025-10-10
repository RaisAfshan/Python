from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from decimal import Decimal
from django.contrib import messages
from Ekartapp.form import userAddressForm
from Ekartapp.models import Product, Category, ProductVariant, ProductVariantImage, Custom_User, UserModel, UserAddress, \
    Coupons, Cart, CartItem, Order, OrderItem, CarouselImage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def user_home(request):
    return render(request,'user/userHome.html')


def user_productHome(request):
    basePrice = ProductVariant.objects.filter(price__lte=80000,product__category__name='Smartphones')[:4]
    category = Category.objects.get(name="Fashion",parent__isnull=True)
    catproduct = ProductVariant.objects.filter(product__category=category,is_default=True)[:4]
    carousel = CarouselImage.objects.filter(is_active=True).order_by('-created_at')
    print(category)
    context = {
        'basePrice': basePrice,
        'carousel':carousel,
        'catproduct':catproduct
    }
    return render(request,'user/userProductHome.html',context)

@login_required(login_url='login1')
def user_cart(request):
    if not request.user.is_authenticated:
        messages.warning(request,'please log in to add items to the cart. ')
        return redirect('login1')
    user = UserModel.objects.get(user=request.user)
    cart = Cart.objects.filter(user=user).first()
    if not cart:
        cart = Cart.objects.create(user=user)
    items = cart.items.all() #  gets all CartItem objects belonging to this Cart

    subtotal = sum(item.total_price for item in items)
    gst = subtotal * Decimal('0.18')
    delivery_charge = Decimal('40.00')
    coupon_discount = Decimal('0.00')

    if cart.coupons and cart.coupons.is_valid:
        if cart.coupons.discount_amount:
            coupon_discount = Decimal(cart.coupons.discount_amount)
        elif cart.coupons.discount_percent:
            coupon_discount = Decimal(subtotal) * Decimal(cart.coupons.discount_percent) / Decimal(100)

    total_price = subtotal+gst+delivery_charge-coupon_discount

    context = {
        'cart':cart,
        'items':items,
        'total_price':total_price,
        'subtotal':subtotal,
        'gst':gst,
        'delivery_charge':delivery_charge,
        'coupon_discount':coupon_discount

    }

    return render(request,'user/cart/userCart.html',context)

@login_required(login_url='login1')
def update_cart_quantity(request,id,action):
    cart_item = get_object_or_404(CartItem,id=id,cart__user__user=request.user)

    if action == 'increase':
        if cart_item.product_variant.quantity > 0:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.warning(request,"no more stock available")
    elif action == 'decrease':
        if cart_item.quantity>1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            messages.warning(request,"item is removed from cart")
    return  redirect('userCart')


@login_required(login_url='login1')
def add_to_cart(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,"please log in to add items to the cart. ")
        return redirect('login1')
    product_variant = get_object_or_404(ProductVariant,id=id)

    if product_variant.quantity<=0:
        messages.error(request,"the item you r selected is out of stock")

    user = UserModel.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=user).first()
    if not cart:
        cart = Cart.objects.create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart,product_variant=product_variant).first()
    if cart_items:
        cart_items.quantity += 1
        cart_items.save()
    else:
        CartItem.objects.create(cart=cart,product_variant=product_variant,quantity=1)

    messages.success(request,"Product added to cart!")
    return redirect('userCart')

@login_required(login_url='login1')
def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get("coupon_code","").strip()
        user = UserModel.objects.get(user=request.user)
        cart, _ = Cart.objects.get_or_create(user=user)

        coupon = Coupons.objects.get(code=code)
        if coupon.is_valid():
            cart.coupons = coupon
            cart.save()
            messages.success(request,f"coupon {coupon.code} coupon is applied succefully")
        else:
            messages.warning(request,f"coupon {coupon.code} coupon is expired")

    return redirect('userCart')



@login_required(login_url='login1')
def couponsUser(request):
    coupons = Coupons.objects.filter(status = True,is_active=True, expiry_date__gte = timezone.now())
    return render(request,'user/cart/all_coupons.html',{'coupons':coupons})

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
        products = ProductVariant.objects.filter(product__category=category,is_default=True).prefetch_related('images')
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

# Order Placed
@login_required(login_url='login1')
def checkout_view(request):
    user = UserModel.objects.filter(user=request.user).first()
    cart = get_object_or_404(Cart, user=user)
    items = cart.items.all()
    address = UserAddress.objects.filter(user=user, is_default=True).first()

    if not address:
        messages.error(request, "Please add a default address before checkout.")
        return redirect('userAddress')

    total = cart.total_price

    context = {
        'cart': cart,
        'items': items,
        'address': address,
        'total': total
    }

    return render(request, 'user/order/checkout.html', context)

@login_required(login_url='login1')
def proceed_order_view(request):
    user = UserModel.objects.filter(user=request.user).first()
    cart = get_object_or_404(Cart,user=user)
    items = cart.items.all()

    if not items.exists():
        messages.warning(request,"your cart is empty")
        return redirect('userCart')

    address = UserAddress.objects.filter(user=user,is_default=True).first()
    if not address:
        messages.error(request,"Please set a default shipping address  before placing an order.")
        return redirect('userAddress')
    total_price = cart.total_price

    order = Order.objects.create(user=user,total_price=total_price,address=address)

    for item in items:
        variant=item.product_variant

        if variant.quantity < item.quantity:
            messages.error(request,f"Insufficient stock only {variant.quantity} left")
            order.delete()
            return redirect('userCart')

        orderItem = OrderItem.objects.create(order=order,product_variant=variant,quantity=item.quantity,price=variant.price)

        variant.quantity -= item.quantity
        variant.save()

    items.delete()
    cart.coupons = None
    cart.save()
    messages.success(request, f"Your order #{order.id} has been placed successfully!")
    return redirect('orderSuccess',id=order.id)

@login_required(login_url='login1')
def order_success_view(request,id):
    order = get_object_or_404(Order,id=id)
    return render(request,'user/order/orderSuccess.html',{'order':order})

@login_required(login_url='login1')
def order_status(request):
    user = UserModel.objects.filter(user=request.user).first()
    orders =Order.objects.filter(user=user).order_by('created_at')
    return render(request,'user/order/orderStatus.html',{'orders':orders})













