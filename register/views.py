from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def register(response):
    form=CreateUserForm()
    if response.method == "POST":
        form=CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
    
    return render(response,"register/register.html",{"form": form})