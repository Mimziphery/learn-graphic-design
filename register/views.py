from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.models import Course, Task, Student
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:    
        form=CreateUserForm()
        if request.method == "POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                userobj = form.save()
                user = form.cleaned_data.get('username')
                tasksAll = Task.objects.all()
                student = Student.objects.create(user= userobj)
                for task in tasksAll:
                    student.tasks.add(task)
                    
                student.save()
                messages.success(request, 'Account was created for '+ user)
                return redirect('/login')
            else:
                print(form.errors)
        
        courses = Course.objects.all()
        return render(request,"register/register.html",{"form": form, "courses": courses})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:   
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, "register/login.html", {})

        courses = Course.objects.all()
        return render(request, "register/login.html", {"courses": courses})

def logoutUser(request):
    logout(request)
    return redirect('/login')