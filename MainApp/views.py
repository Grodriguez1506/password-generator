from django.shortcuts import render
import random
from django.contrib import messages

# Create your views here.

def inicio(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('-_+!@#$%^&*()')
    if request.GET.get('numbers'):
        characters.extend('0123456789')

    for x in range(length):
        generated_password += random.choice(characters)

    messages.success(request,'The password has been generated successfully')
    return render(request, 'password.html', {
        'password':generated_password
    }) 