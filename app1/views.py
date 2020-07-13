from django.shortcuts import render,redirect
from django.contrib import messages



def index(request):
    return render(request,"index.html")


def adminlogin(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")

    if un == "lala" and  pa == "Lala1":
        return render(request,"admin_home.html")
    else:
        msg = {"error":"Invalid User"}
        return render(request,"admin_login.html",message=msg)


def newclass(request):

    return render(request,'newclass.html')
