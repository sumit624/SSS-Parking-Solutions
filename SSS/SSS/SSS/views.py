import email
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from form.models import savedata

def bookslot(request):
    return render(request, "book.html")

def homepage(request):
    return render(request,"index.html")

def show(request):
    return HttpResponse("sumit")

def location(request):
    return render(request, 'location.html')

def register(request):
    return render(request, 'register.html')

def savedatas(request):
    if request.method=="POST":
        name=request.POST.get('name')
        vehicle_no=request.POST.get('vehicle')
        license_no=request.POST.get('license')
        aadhar_no=request.POST.get('aadhar')
        model=request.POST.get('model')
        global email
        global password
        email=request.POST.get('email')
        password=request.POST.get('password')

        en=savedata(name=name,vehicle_no=vehicle_no,license_no=license_no,
        aadhar_no=aadhar_no,model=model,email=email,password=password)
        en.save()
    return render(request,"index.html")

def verifydata(request):

    if request.method=="POST":
        loginemail=request.POST.get('loginemail')
        loginpass=request.POST.get('loginpass')
        

        if loginemail==email:
            if loginpass==password:
                output=print("Login Success")
            else:
                output=print("Invalid Email or Password")

    return render(request,"index.html")


def tray(request):
    return render(request, "tray.html")