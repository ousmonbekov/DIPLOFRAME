from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ======================
# HOME
# ======================
def index(request):
    return render(request, 'index.html')


# ======================
# LOGIN
# ======================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username yoki parol noto‘g‘ri')

    return render(request, 'login.html')


# ======================
# REGISTER
# ======================
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Parollar mos emas')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bunday foydalanuvchi mavjud')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect('profile')

    return render(request, 'register.html')


# ======================
# PROFILE
# ======================
@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')


# ======================
# LOGOUT
# ======================
def logout_view(request):
    logout(request)
    return redirect('login')
