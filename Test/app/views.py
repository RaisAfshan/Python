from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from app.Forms import UserRegister, CustomUser_Reg, TaskForm
from app.filter import TaskFilter
from app.models import TaskUser, Tasks


@login_required(login_url='log')
def user_dash(request):
    user = TaskUser.objects.filter(user=request.user).first()
    return render(request,'user_dash.html',{'tuser':user})

def user_regForm(request):
    customForm = CustomUser_Reg()
    userForm = UserRegister()
    if request.method == 'POST':
        customForm = CustomUser_Reg(request.POST)
        userForm = UserRegister(request.POST)
        if customForm.is_valid() and userForm.is_valid():
            uType = customForm.save(commit=False)
            uType.is_user = True
            uType.save()

            userObj = userForm.save(commit=False)
            userObj.user = uType
            userObj.save()
            return redirect('log')
    return render(request,'user_register.html',context={'customForm':customForm,'userForm':userForm})

def userLogin(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            if user.is_user:
                return redirect('user_dash1')
    return render(request,'login.html')

def logOut(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def addTask(request):
    taskForm = TaskForm()
    user = TaskUser.objects.filter(user=request.user).first()
    if request.method == 'POST':
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid():
            taskObj = taskForm.save(commit=False)
            taskObj.user = user
            taskObj.save()
            return redirect('TaskList1')
    return render(request,'addTask.html',context={'taskForm':taskForm})

@login_required(login_url='log')
def TaskList(request):
    user = TaskUser.objects.filter(user=request.user).first()
    tasks = Tasks.objects.filter(user=user)

    #Search
    taskFilter = TaskFilter(request.GET,queryset=tasks)
    tasks = taskFilter.qs

    #Paginator
    paginator= Paginator(tasks,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'taskList.html',{'tasks':page_obj,'taskFilter':taskFilter})

@login_required(login_url='log')
def Taskedit(request,id):
    editData = Tasks.objects.get(id=id)
    if request.method== 'POST':
        updateTask = TaskForm(request.POST,instance=editData)
        if updateTask.is_valid():
            updateTask.save()
            return redirect('TaskList1')
    else:
        updateTask = TaskForm(instance=editData)
    return render(request,'editForm.html',{'updateTask':updateTask})

@login_required(login_url='log')
def taskDelete(request,id):
    Tasks.objects.get(id=id).delete()
    return redirect('TaskList1')











