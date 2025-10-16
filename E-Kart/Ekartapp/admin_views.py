from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from Ekartapp.adminFilter import ProductVariantFilter
from Ekartapp.form import CategoryForm, ProductForm, UserForm, VariantTypeForm, \
    VariantsForm, ProductVariantForm
from Ekartapp.models import Category, Product, UserModel, VariantType, Variants, ProductVariant


@login_required(login_url='login1')
def admin_dashboard(request):
    return render(request,'admin/adminDashboard.html')

# Product Category
@login_required(login_url='login1')
def category_view(request):
    category_form = CategoryForm()
    if request.method == 'POST':
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,'category updated successfully ')
            return redirect('categoryDisplay')
        else:
            messages.error(request,'error updating category')
    return render(request,'admin/categoryForm.html',{'category_form':category_form})

@login_required(login_url='login1')
def categoryDisplay(request):
    categoreis = Category.objects.filter(status=True).order_by('-created_at')
    return render(request,'admin/categoriesDisplay.html',{'categories':categoreis})

@login_required(login_url='login1')
def category_edit(request,id):
    edit_category = Category.objects.get(id=id)
    if request.method == 'POST':
        edit_form = CategoryForm(request.POST,instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()

            return redirect('categoryDisplay')
    else:
        edit_form = CategoryForm(instance=edit_category)
    return render(request,'admin/edit_category.html',{'edit_form':edit_form})

@login_required(login_url='login1')
def category_delete(request,id):
    deleteData = Category.objects.get(id=id)
    deleteData.status = False
    deleteData.save()

    for sub in deleteData.subcategory.all():
        sub.status = False
        sub.save()
    messages.warning(request, 'Category being deleted')
    return redirect('categoryDisplay')

# Product CRUD
@login_required(login_url='login1')
def product_add(request):
    Pform = ProductForm()
    if request.method == 'POST':
        pform = ProductForm(request.POST)
        if pform.is_valid():
            prod = pform.save(commit=False)
            prod.created_by = request.user
            prod.status = True
            prod.save()
            messages.success(request, "Product added successfully")
            return redirect('productDisplay')
        else:
            messages.error(request,"error while adding products")
    return render(request,'admin/productAddForm.html',{'Pform':Pform})

@login_required(login_url='login1')
def product_view(request):
    products = Product.objects.filter(status=True,created_by=request.user).order_by('-created_at')
    return render(request,'admin/productDisplay.html',{'products':products})

@login_required(login_url='login1')
def product_edit(request,id):
    editData = Product.objects.get(id=id)
    if request.method == 'POST':
        pform = ProductForm(request.POST,instance=editData)
        if pform.is_valid():
            pform.save()
            return redirect('productDisplay')
    else:
        pform = ProductForm(instance=editData)
    return render(request,'admin/productEditForm.html',{'pform':pform})

@login_required(login_url='login1')
def product_delete(request,id):
    product_data = Product.objects.get(id=id)
    product_data.status = False
    product_data.save()
    return redirect('productDisplay')

@login_required(login_url='login1')
def variant_type_view(request):
    variant = VariantType.objects.filter(status=True)
    return render(request,'admin/VariantType/variant_type.html',{'variant_type':variant})


@login_required(login_url='login1')
def variant_type_add(request):
    Vform = VariantTypeForm
    if request.method == 'POST':
        Vform = VariantTypeForm(request.POST)
        if Vform.is_valid():
            Vform.save()
            messages.success(request, 'variant type added successfully ')
            return redirect('variantDisplay')
        else:
            messages.error(request,'failed to add')
    return render(request,'admin/VariantType/variantTypeAdd.html',{'Vform':Vform})

@login_required(login_url='login1')
def variant_type_edit(request,id):
    var_type = get_object_or_404(VariantType,id=id)
    if request.method == 'POST':
        Vform = VariantTypeForm(request.POST,instance=var_type)
        if Vform.is_valid():
            Vform.save()
            messages.success(request, 'variant type updated successfully ')
            return redirect('variantDisplay')
        else:
            messages.error(request,'variant type update failed')
    else:
        Vform = VariantTypeForm(instance=var_type)
    return render(request,'admin/VariantType/variantTypeEdit.html',{'Vform':Vform})

@login_required(login_url='login1')
def variant_type_delete(request,id):
    var_type = get_object_or_404(VariantType,id=id)
    var_type.status = False
    var_type.save()
    messages.success(request,'deleted successfully')
    return redirect('variantDisplay')

@login_required(login_url='login1')
def variant_value_add(request):
    valueForm = VariantsForm()
    if request.method == 'POST':
        valueForm = VariantsForm(request.POST)
        if valueForm.is_valid():
            valueForm.save()
            messages.success(request, 'variant value added successfully ')
            return redirect('variantValueDisplay')
        else:
            messages.error(request, 'failed to add')
    return render(request,'admin/VariantType/add_variant.html',{'valueForm':valueForm})

@login_required(login_url='login1')
def variant_value_edit(request,id):
    value_id = get_object_or_404(Variants,id=id)
    if request.method == 'post':
        valueForm = VariantsForm(request.POST,instance=value_id)
        if valueForm.is_valid():
            valueForm.save()
            messages.success(request, 'variant value updated successfully ')
            return redirect('variantValueDisplay')
        else:
            messages.error(request, 'failed to update')
    else:
        valueForm = VariantsForm(instance=value_id)
    return render(request,'admin/VariantType/edit_variant.html',{'valueForm':valueForm})


@login_required(login_url='login1')
def variant_value_display(request):
    variants = VariantType.objects.filter(status=True).prefetch_related(Prefetch('variants',queryset=Variants.objects.filter(status=True)))
    return render(request,'admin/VariantType/variant_values.html',{'variants':variants})

@login_required(login_url='login1')
def variant_value_delete(request,id):
    value_id = get_object_or_404(Variants,id=id)
    value_id.status = False
    value_id.save()
    return redirect('variantValueDisplay')

# Product Variant Crud
@login_required(login_url='login1')
def product_variant_display(request):
    product_variants = ProductVariant.objects.filter(status=True,product__status=True,product__primary_variant__status=True,primary_variant__status=True).order_by('-created_at')
    filter_product_variant = ProductVariantFilter(request.GET,queryset=product_variants)
    product_variants = filter_product_variant.qs
    return render(request,'admin/variant/productVariantDisplay.html',{'product_variants':product_variants,'filter_product_variant':filter_product_variant})

@login_required(login_url='login1')
def product_variant_add(request,id):
    product = get_object_or_404(Product,id=id)

    primary_variants = Variants.objects.filter(variant_type=product.primary_variant,status=True)
    secondary_variants = Variants.objects.none()
    if product.secondary_variant:
        secondary_variants = Variants.objects.filter(variant_type=product.secondary_variant,status=True)

    if request.method == 'POST':
        prod_var_form = ProductVariantForm(request.POST)
        if prod_var_form.is_valid():
            prod_var = prod_var_form.save(commit=False)
            prod_var.product = product
            prod_var.save()
            messages.success(request, 'Product variant added successfully ')
            return redirect('productVariantDisplay')
        else:
            messages.error(request, 'failed to add ')
    else:
        prod_var_form = ProductVariantForm()

    prod_var_form.fields['primary_variant'].queryset  = primary_variants
    prod_var_form.fields['secondary_variant'].queryset = secondary_variants

    return render(request,'admin/variant/productVariantAdd.html',{'prod_var_form':prod_var_form,'product':product})

@login_required(login_url='login1')
def product_variant_edit(request, id):
    product_var = get_object_or_404(ProductVariant, id=id)
    product = product_var.product

    primary_variants = Variants.objects.filter(variant_type=product.primary_variant, status=True)
    secondary_variants = Variants.objects.none()
    if product.secondary_variant:
        secondary_variants = Variants.objects.filter(variant_type=product.secondary_variant, status=True)

    if request.method == 'POST':
        form = ProductVariantForm(request.POST, instance=product_var)
        if form.is_valid():
            form.save()
            return redirect('productVariantDisplay')
    else:
        form = ProductVariantForm(instance=product_var)

    form.fields['primary_variant'].queryset = primary_variants
    form.fields['secondary_variant'].queryset = secondary_variants

    return render(request, 'admin/variant/editVariantProduct.html', {'prod_var_edit': form})

@login_required(login_url='login1')
def product_variant_delete(request,id):
    product_var_id = get_object_or_404(ProductVariant,id=id)
    product_var_id.status = False
    product_var_id.save()
    return redirect('productVariantDisplay')

# Product Image
@login_required(login_url='login1')
def product_images_display(request):
    return render(request,'admin/productImage/productImageDisplay.html')

@login_required(login_url='login1')
def product_image_add(request):
    return render(request,'admin/productImage/imageAdd.html')

@login_required(login_url='login1')
def product_image_edit(request):
    return render(request,'admin/productImage/imageEdit.html')

@login_required(login_url='login1')
def product_image_delete(request):
    pass

# Order Status
@login_required(login_url='login1')
def orderStatus(request):
    return render(request,'admin/order/orderStatus.html')

@login_required(login_url='login1')
def orderEdit(request):
    return render(request,'admin/order/orderStatusEdit.html')

# admin products overview
@login_required(login_url='login1')
def admin_products_overview(request):
    return render(request,'admin/productCard/adminProducts.html')

# admin user view
@login_required(login_url='login1')
def admin_user_view(request):
    userData = UserModel.objects.filter(status=True)
    return render(request,'admin/user/adminUserView.html',{'userData':userData})

@login_required(login_url='login1')
def admin_user_edit(request,id):
    user_id = get_object_or_404(UserModel,id=id)
    if request.method == 'POST':
        uform =UserForm(request.POST,instance=user_id)
        if uform.is_valid():
            uform.save()
            return redirect('adminUser')
    else:
        uform = UserForm(instance=user_id)
    return render(request,'admin/user/userEdit.html',{'uform':uform})

@login_required(login_url='login1')
def user_delete(request,id):
    user_id = get_object_or_404(UserModel,id=id)
    print(user_id.status)
    user_id.status = False
    user_id.save()
    return redirect('adminUser')

# Banner CRUD
@login_required(login_url='login1')
def add_banner(request):
    return render(request,'admin/banner/addBanner.html')

@login_required(login_url='login1')
def banner_display(request):
    return render(request,'admin/banner/BannerList.html')

@login_required(login_url='login1')
def banner_edit(request):
    return render(request,'admin/banner/BannerEdit.html')


@login_required(login_url='login1')
def banner_delete(request):
    pass

# Admin Home page
@login_required(login_url='login1')
def admin_homepage(request):
    return render(request,'admin/AdminHomePage.html')











