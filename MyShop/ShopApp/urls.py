from django.urls import path
from . import views

urlpatterns=[
    path('welcome/',views.this_shop),
    path('home/',views.homepage),
    path('contact/',views.contact),
    path('about/',views.about),
    path('order/',views.order)
]