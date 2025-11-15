from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard.index')

        messages.error(request, "Username atau password salah.")

    return render(request, "users/login.html")


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    return render(request, "users/index.html")
