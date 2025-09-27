from django.shortcuts import render,redirect
from django.contrib import messages
from Ekartapp.form import CategoryForm
from Ekartapp.models import Category


def admin_dashboard(request):
    return render(request,'admin/adminDashboard.html')

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

def categoryDisplay(request):
    categoreis = Category.objects.filter(status=True).order_by('-created_at')
    return render(request,'admin/categoriesDisplay.html',{'categories':categoreis})

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

def category_delete(request,id):
    deleteData = Category.objects.get(id=id)
    deleteData.status = False
    deleteData.save()

    for sub in deleteData.subcategory.all():
        sub.status = False
        sub.save()
    messages.warning(request, 'Category being deleted')
    return redirect('categoryDisplay')



