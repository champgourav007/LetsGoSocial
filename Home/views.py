from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request, 'Home/index.html')

def userHome(request):
    return render(request, 'Home/userHome.html')

def loginUser(request):
    if request.method == "POST":
        data = request.POST
        try:
            user = User.objects.get(email = str(data['email']))
            if user.email:
                password = data["password"]
                if not user.password:
                    user.set_password(data["password"])
                    user.save()
                authenticated_user = auth.authenticate(request, email=data['email'], password=password)
                if not authenticated_user:
                    return render(request, 'Auth/login.html', context={
                        "error_message" : "Wrong Password"
                    })
                auth.login(request, authenticated_user)
                return render(request, 'Home/userHome.html', context={
                    "alert_message" : "Welcome, " + str(user.get_full_name())
                })
            else:
                return render(request, 'Auth/login.html', context={
                    "error_message" : "You are not Savages!!! Sorry You can not Login"
                })
        except:
            return render(request, 'Auth/login.html', context={
                    "error_message" : "You are not Savages!!! Sorry You can not Login"
                }) 
    else:
        return redirect('userHome')
