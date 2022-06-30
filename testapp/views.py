from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def register(request):
    return render(request,"registration.html")


def save_user(request):
    name=request.POST.get('c1')
    pwd=request.POST.get('c2')
    User(User_Name=name,User_Pwd=pwd).save()
    return redirect("register")
def trackgoods(request):
    return render(request,'trackgoods.html')


def locatetat(request):
    return render(request,"Location.html")


def contactus(request):
    return render(request,"contact.html")


def login(request):
    nam=request.GET.get('l1')
    pas=request.GET.get('l2')
    data=User.objects.all()

    return render(request,'login.html')