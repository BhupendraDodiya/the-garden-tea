from django.shortcuts import render, redirect
from app .models import *
from django.http.response import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    item = Product.objects.all()
    return render(request, "home.html",{'item':item})


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def infor(request):
    if request.method == 'POST':
        na = request.POST['name']
        em = request.POST['email']
        su = request.POST['subject']
        me = request.POST['message']
        Contact.objects.create(name=na, email=em, subject=su, message=me)
        messages.success(request, "Your feedback has been received, you will get a response soon.")
        return redirect('/contact/')
