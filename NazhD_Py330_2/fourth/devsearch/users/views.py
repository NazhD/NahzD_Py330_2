from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_user(request):
    error = None
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            error = "Имя пользователя не существует"

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            error = "Не верный логин или пароль"
    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')


def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)
    top_skills = prof.skill_set.exclude(description__exact="")
    other_skills = prof.skill_set.filter(description="")
    context = {
        "profile": prof,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    return render(request, "users/profile.html", context)
