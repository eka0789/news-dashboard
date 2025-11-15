from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# ==============================
# LOGIN & LOGOUT
# ==============================
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


# ==============================
# LIST USER
# ==============================
@login_required
def user_list(request):
    users = User.objects.all().order_by('id')
    return render(request, "users/user_list.html", {"users": users})


# ==============================
# CREATE USER
# ==============================
@login_required
def user_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        # cek username duplikat
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan.")
            return redirect("users.create")

        # buat user baru
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Role handling
        if role == "admin":
            user.is_staff = True
            user.is_superuser = True
        elif role == "staff":
            user.is_staff = True
            user.is_superuser = False
        else:
            user.is_staff = False
            user.is_superuser = False

        user.save()

        messages.success(request, "User berhasil ditambahkan.")
        return redirect("users.index")

    return render(request, "users/user_create.html")


# ==============================
# EDIT USER
# ==============================
@login_required
def user_edit(request, id):
    user_obj = get_object_or_404(User, id=id)

    if request.method == "POST":
        user_obj.username = request.POST.get("username")
        user_obj.email = request.POST.get("email")
        role = request.POST.get("role")
        password = request.POST.get("password")

        # Atur role
        if role == "admin":
            user_obj.is_staff = True
            user_obj.is_superuser = True
        elif role == "staff":
            user_obj.is_staff = True
            user_obj.is_superuser = False
        else:
            user_obj.is_staff = False
            user_obj.is_superuser = False

        # Update password jika diisi
        if password.strip() != "":
            user_obj.set_password(password)

        user_obj.save()

        messages.success(request, "User berhasil diperbarui.")
        return redirect("users.index")

    return render(request, "users/user_edit.html", {"user_obj": user_obj})


# ==============================
# DELETE USER
# ==============================
@login_required
def user_delete(request, id):
    user_obj = get_object_or_404(User, id=id)

    # cegah menghapus dirinya sendiri
    if request.user.id == user_obj.id:
        messages.error(request, "Tidak bisa menghapus akun Anda sendiri.")
        return redirect("users.index")

    user_obj.delete()
    messages.success(request, "User berhasil dihapus.")
    return redirect("users.index")
