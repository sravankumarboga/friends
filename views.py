from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import details
from django.urls import reverse
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def detail(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        
        if details.objects.filter(user_name=username).exists():
            messages.info(request," this user name allready exists")
            return redirect("register")
        elif details.objects.filter(password1 = password2).exists():
            messages.info(request,"password is not maching please check it agin")
            return redirect("register")
        elif details.objects.filter(mobile=mobile).exists():
            messages.info(request," this mobile number  allready exists")
            return redirect("register")
        elif details.objects.filter(email=email).exists():
            messages.info(request," this email address  allready exists")
            return redirect("register")
        elif details.objects.filter(address=address).exists():
            messages.info(request,"please enter your address")
            return redirect("register")
        elif details.objects.filter(first_name=first_name).exists():
            messages.info(request,"please enter your first name")
            return redirect("register")
        elif details.objects.filter(last_name=last_name).exists():
            messages.info(request,"please Enter your last name")
            return redirect("register")
        
    
        else:
            user = details.objects.create(user_name=username,password1=password1,password2=password2,first_name=first_name,last_name=last_name,email=email,address=address,mobile=mobile)
            user.save()
            print("user created")
            return redirect("login")
    else:
        return render(request,"register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user_details = authenticate(user_name=username,password2=password)
        if details.objects.filter(user_name=username).exists()and details.objects.filter(password1=password).exists():
            #auth.login(request,user_details)
            return redirect("/")
        else:
            messages.info(request, "Your username and password are incorrect. Please try again.")
            return redirect("login")
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")