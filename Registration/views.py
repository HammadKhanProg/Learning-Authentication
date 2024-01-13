from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="signin")
def home (request):
    return render (request,"home.html")

def signup (request):
    try:
        if request.method=="POST":
            uname=request.POST.get("username")
            email=request.POST.get("email")
            pass1=request.POST.get("password1")
            pass2=request.POST.get("password2")
            if pass1 != pass2:
                return HttpResponse ("Your password And Confirm Password does not match")
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect ("signin")
    except:
        pass
    return render(request,"signup.html")

def signin (request):
    try:
        if request.method=="POST":
            uname=request.POST.get("username")
            pass1=request.POST.get("pass")
            user=authenticate(request,username=uname,password=pass1)
            if user is not None:
                login(request,user)
                return redirect ("home")
            else:
                return render ("Username or Password Incorrect")

            return redirect("home")

    except:
        pass
    return render(request,"signin.html")

def logoutpage (request):
    logout(request)
    return redirect("signin")