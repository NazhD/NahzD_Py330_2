from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def reg(request):
    if request.method == 'GET':
        return render(request, 'avtoreg/reg.html',
                      {"form": UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                return redirect('loginuser')
            except IntegrityError:
                return render(request, 'avtoreg/reg.html', {
                    "form": UserCreationForm,
                    'error': "Существует"})
        else:
            print("пароли не совпали")
            return render(request, 'avtoreg/reg.html',
                          {"form": UserCreationForm,
                           'error': "пароли не совпали"})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def loginuser(request):
    if request.method == 'GET':
        return render(request, "avtoreg/loginuser.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, "avtoreg/loginuser.html",
                          {"form": AuthenticationForm(),
                           "error": "не верные данные для входа"})
        else:
            login(request, user)
            return redirect('index')





