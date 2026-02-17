from django.shortcuts import render,redirect
from .models import Task
from .forms import Add_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task_view(request):
    data =Task.objects.all()
    return render(request,'task.html',{'data':data})

def delete_view(request,id):
    data = Task.objects.get(id=id)
    data.delete()
    return redirect('task')

def add_view(request):
    if request.method =="POST":
        entering_details = Add_form(request.POST)
        if entering_details.is_valid():
            entering_details.save()
            return redirect('task')
    else:
        entering_details = Add_form()
    return render(request,"add.html",{'entering_details':entering_details})

def edit_view(request,id):
    record = Task.objects.get(id=id)
    if request.method =='POST':
        entering_details = Add_form(request.POST,instance = record)
        if entering_details.is_valid():
            entering_details.save()
            return redirect('task')
    else:
        entering_details = Add_form(instance=record)
    return render(request,'add.html',{"entering_details":entering_details})


def register_view(request):
    if request.method=="POST":
        user_form = UserCreationForm(request.POST)
        # user = user_form.save()
        if user_form.is_valid():
            user = user_form.save()
            login(request,user)
            return redirect('login')
            
    else:
        user_form = UserCreationForm()
       
    return render(request,'register.html',{'user_form':user_form})

def login_view(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('task')
        else:
            return render(request,'login.html',{'error':"Invalid credentials"}) 
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')