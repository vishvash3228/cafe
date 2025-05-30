from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def index(request):
    form = tableform()  # Initialize form for GET requests
    if request.method == "POST":
        form = tableform(request.POST)
        if form.is_valid():
            form.save()
            print("Your Order Has Been Submitted!!")
            
        else:
            print(form.errors)
    return render(request, "index.html", {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, f"{form.errors[field][0]}")
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})