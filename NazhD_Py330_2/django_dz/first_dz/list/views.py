from django.shortcuts import render, get_object_or_404
from .models import ListTexter
from django.http import HttpRequest
import re


def list_texter(request):
    textures = ListTexter.objects.all()
    return render(request, 'list/index.html', {'textures': textures})


def typetexter(request, type):
    textures = ListTexter.objects.all()
    return render(request, 'list/metal.html', {'textures': textures,'type': type} )







