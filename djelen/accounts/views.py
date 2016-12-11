from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterUserForm, Login
from django.contrib import messages
from django.db.utils import *


def registration(request):
    print('registration')
    login_form = Login()
    user_form = RegisterUserForm()
    if request.POST:
        print('post')
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            try:
                user = User.objects.create_user(username=user_form.cleaned_data['username'],
                                                email=user_form.cleaned_data['email'],
                                                password=user_form.cleaned_data['password'],
                                                first_name=user_form.cleaned_data['first_name'],
                                                last_name=user_form.cleaned_data['last_name']
                                                )
                user.save()
                messages.success(request, "Registranion ok")
                return redirect('/')
            except IntegrityError:
                print('!!!')
                messages.success(request, "Користувач з таким логіном вже існує!")
        else:
            messages.success(request, 'Введено не коректні дані')
    print('render', user_form)
    return render(request, 'registration.html', {'user_form': user_form, 'login_form': login_form})


def log_in(request):
    print('log_in')
    if request.POST:
        login_form = Login(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Login ok')
            else:
                messages.success(request, 'Invalid login')
            return redirect('/')


def log_out(request):
    print(log_out)
    if request.POST:
        logout(request)
        return redirect('/')
