from django.shortcuts import render
from django.http import HttpResponse
from package.models import Package
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
def Services(request):
       return render(request,'services.html')
def hello(request):
       return render(request,'hello.html')
