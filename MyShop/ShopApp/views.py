from django.shortcuts import render
from django.http import HttpResponse

def this_shop(request):
    return HttpResponse("Welcome to our shop!!!")

def homepage(request):
    page={"home":"Home Page","content":"A shop , Thousands of happiness"}
    return render(request,"index.html",page)

def contact(request):
    email="contact@example.com",
    social_profiles=[
        "Facebook: fb.m\example",
        "Twitter: hello.\tweet",
        "LinedIN: nowshin.\linkedin"
    ]
    return render(request,"contact.html",{"emailaddress":email},{"socialprofiles":social_profiles})

def about(request):
    return render(request,"about.html")

def order(request):
    return render(request,"order.html")
