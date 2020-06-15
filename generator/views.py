import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    info = {
        "name": "Ritesh Gajera",
    }
    return render(request, 'generator/about.html', {'data':info})


def password(request):
    
    password = ""
    characters = list('abcdefghijklmnopgerstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?'))

    length = int(request.GET.get('length'))
    for x in range(length):
        password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': password})
