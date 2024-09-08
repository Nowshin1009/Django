from django.shortcuts import render
from django.http import HttpResponse

def this_shop(request):
    return HttpResponse("Welcome to our shop!!!")

def homepage(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def order(request):
    return render(request,"order.html")
