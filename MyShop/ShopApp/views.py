from django.shortcuts import render
from django.http import HttpResponse

def this_shop(request):
    return HttpResponse("Welcome to our shop!!!")

def homepage(request):
    page={"home":"Home Page","content":"A shop , Thousands of happiness"}
    return render(request,"index.html",page)

def contact(request):
    page={"contact":"Contact Us","content":"A shop , Thousands of happiness"}
    email="contact@example.com",
    social_profiles=[
        "Facebook: fb.m\example",
        "Twitter: hello.\tweet",
        "LinedIN: nowshin.\linkedin"
    ]
    return render(request,"contact.html",page,{"emailaddress":email},{"socialprofiles":social_profiles})

def about(request):
    page={"about":"About","content":"A shop , Thousands of happiness"}
    return render(request,"about.html",page)

def order(request):
    page={"Order":"Order","content":"A shop , Thousands of happiness"}
    return render(request,"order.html",page)
