from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

def login(request, type):
    if type == "savages":
        return render(request, 'Auth/login.html', context={
            "type" : "Savages"
        })
    return render(request, 'Auth/login.html')

def logout(request):
    pass

def getPassword(request):
    pass