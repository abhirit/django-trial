from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'aks'})

def add(request):
    res = int(request.POST["num1"]) + int(request.POST["num2"])
    return render(request, 'home.html', {'res':res, 'name' : 'aks'} )