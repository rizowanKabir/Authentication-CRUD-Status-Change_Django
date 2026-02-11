from django.shortcuts import render,redirect
from .models import UserInfoModel, TaskModel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'home.html')
def register_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_exists = UserInfoModel.objects.filter(username=username).exists()
        if user_exists:
            messages.warning(request,'Username already exists in database')
            return redirect('register_page')
        if password == confirm_password:
            UserInfoModel.objects.create_user(
                full_name = full_name,
                username = username,
                email = email,
                user_type = user_type,
                password = password,
            )
            return redirect('login_page')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            messages.success(request, 'Login Successfully')
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid Credentials.Try wright information') 
            return redirect('login_page')   

    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required
def dashboard(request):

    return render(request, 'dashboard.html')

@login_required
def task_list(request):
    current_user = request.user
    current_user_type = request.user.user_type
    if current_user_type == 'Admin':
        task_data = TaskModel.objects.all()
    else:
        task_data = TaskModel.objects.filter(created_by = current_user)    
    context_dict = {
        'task_data': task_data,
    }
    return render(request, 'task_list.html', context_dict)

@login_required
def add_task(request):
    if request.method =='POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_status = request.POST.get('task_status')
        deadline = request.POST.get('deadline')
        current_user = request.user

        TaskModel.objects.create(
            task_name = task_name,
            task_description = task_description,
            task_status = task_status,
            deadline = deadline,
            created_by = current_user
        )
        return redirect('task_list')

    return render(request, 'add_task.html')

@login_required
def edit_task(request,task_id):

    edit_task = TaskModel.objects.get(id = task_id)
    if request.method =='POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_status = request.POST.get('task_status')
        deadline = request.POST.get('deadline')
        current_user = request.user

        TaskModel(
            id = task_id, 
            task_name = task_name,
            task_description = task_description,
            task_status = task_status,
            deadline = deadline,
            created_by = current_user
        ).save()
        return redirect('task_list')

    context_dict = {
        'edit_task': edit_task
    }
    return render(request, 'edit_task.html', context_dict)

@login_required
def delete_task(request,task_id):
    TaskModel.objects.get(id = task_id).delete()
    return redirect('task_list')

def change_status(request,task_id):
    task = TaskModel.objects.get(id = task_id)
    if task.task_status == 'NotStarted':
        task.task_status = 'InProgress'
    elif task.task_status == 'InProgress':
        task.task_status = 'Completed'   
    task.save()

    return redirect('task_list')
