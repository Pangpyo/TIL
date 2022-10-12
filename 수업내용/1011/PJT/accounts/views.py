from multiprocessing import context
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:index")


def profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/profile.html", context)


def userlist(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/userlist.html", context)
