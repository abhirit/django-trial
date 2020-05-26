from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'pwd.html')

def password(request):
    character=list('abcdefghijklmnopqrstuvwxyz')
    lenth = int(request.POST.get('length'))
    if request.POST.get('uppercase') :
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.POST.get('special') :
        character.extend(list("!@#$%^&*"))
    if request.POST.get('numbers') :
        character.extend(list("0123456789"))
    pswd = ''
    for x in range(lenth):
        x=x
        pswd+=random.choice(character)
    return render(request,'pwd.html', {'pswd' : pswd})
