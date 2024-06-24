from django.shortcuts import render , HttpResponse
from datetime import datetime
from DB.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def home(request):
    return render(request, 'index.html')

def notes(request):
    return render(request, 'notes.html')

def course(request):
    return render(request, 'course.html')


def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        problem= request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, problem=problem, date=datetime.today())
        contact.save()
        messages.success(request, "Your messege has been sent. We will contact you soon...")
    return render(request, 'contact.html')
    #return HttpResponse("this is contact us page")

def services(request):
    return render(request, 'services.html')
