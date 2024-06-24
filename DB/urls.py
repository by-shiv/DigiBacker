from django.contrib import admin
from django.urls import path
from DB import views

urlpatterns = [
    path("", views.home, name='homepage'),
    path("home", views.home, name='homepage'),
    path("contact", views.contact, name='contactus'),
    path("services", views.services, name='services'),
    #path("notes", views.notes, name='notes') 
]