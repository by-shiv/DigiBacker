from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='dashboard'),
    path('dashboard',views.index,name='dashboard'),
    path("home", views.home, name='homepage'),
    path("contact", views.contact, name='contactus'),
    path("services", views.services, name='services'),
    path("notes", views.notes, name='notes') 
]