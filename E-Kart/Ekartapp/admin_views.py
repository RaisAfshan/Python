from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from Ekartapp.form import CategoryForm, ProductForm
from Ekartapp.models import Category, Product

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
            return redirect('product_display')
        else:
            messages.error(request,"error while adding products")
    return render(request,'admin/productAddForm.html',{'Pform':Pform})

@login_required(login_url='login1')
def product_view(request):
    products = Product.objects.filter(status=True,created_by=request.user)
    return render(request,'admin/productDisplay.html',{'products':products})

@login_required(login_url='login1')
def product_edit(request,id):
    editData = Product.objects.get(id=id)
    if request.method == 'POST':
        pform = ProductForm(request.POST,instance=editData)
        if pform.is_valid():
            pform.save()
            return redirect('product_display')
    else:
        pform = ProductForm(insatnce=editData)
    return render(request,'admin/productEditForm.html',{'pform':pform})

@login_required(login_url='login1')
def product_delete(request,id):
    product_data = Product.objects.get(id=id)
    product_data.status = False
    product_data.save()
    return redirect('product_display')

# Product Variant Crud
@login_required(login_url='login1')
def product_variant_display(request):
    return render(request,'admin/variant/productVariantDisplay.html')

@login_required(login_url='login1')
def product_variant_add(request):
    return render(request,'admin/variant/productVariantAdd.html')

@login_required(login_url='login1')
def product_variant_edit(request):
    return render(request,'admin/variant/editVariantProduct.html')

@login_required(login_url='login1')
def product_variant_delete(request):
    pass

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
    return render(request,'admin/user/adminUserView.html')

@login_required(login_url='login1')
def add_banner(request):
    return render(request,'admin/banner/addBanner.html')

@login_required(login_url='login1')
def banner_display(request):
    return render(request,'admin/banner/addBanner.html')










