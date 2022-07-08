from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
# import this module here for show messages in website
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        PhoneNumber = request.POST.get('PhoneNumber')
        Password = request.POST.get('Password')
        desc = request.POST.get('desc')
        contact = Contact(FirstName=FirstName, LastName=LastName, Email=Email, PhoneNumber=PhoneNumber, Password=Password, desc=desc, date=datetime.today())
        contact.save()
        # show this messages after submit contact from
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')