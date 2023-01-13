from django.shortcuts import render
from django.http import HttpResponse
from package.models import Package
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives

# Create your views here.
def index(request):
       fatch=Package.objects.all().order_by('-id')[:3]
       print(fatch[0].Title)
       contex={
              "item":fatch
       }
       request.session['name']="ghelo"
       
       return render(request,'index.html' ,contex)
def about(request):
       return render(request,'about.html')

def contact(request):
       if request.method=='POST':
              name=request.POST.get('name')
              email=request.POST.get('email')
              message=request.POST.get('massage')
              new=Contact()
              new.FullName=name
              new.Email=email
              new.Message=message
              new.save()
              messages.error(request,"Ok")
       return render(request,'contact.html')
