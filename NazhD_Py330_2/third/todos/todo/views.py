from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'todo/home.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request,
                             username=request.POST['username'],
                             password=request.POST['password'])
        if user is None:
            return render(request,
                          'todo/loginuser.html',
                          {'form': AuthenticationForm(), "error": "не верные данные"})
        else:
            login(request, user)
            return redirect('currenttodes')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def signupuser(request):
    if request.method =='GET':
        return render(request,
                      'todo/signupuser.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodes')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': "Существует"})

        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': "пароли не совпали"})


def currenttodes(request):
    return render(request, 'todo/currenttodes.html')
