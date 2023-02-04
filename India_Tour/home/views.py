from django.shortcuts import render,redirect
from django.http import HttpResponse
from package.models import Package
from .models import Contact
from users.models import Count,Customer
import requests
import json
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives

# Create your views here.
def index(request):
       data=Count.objects.all().values()
       totalvisitor=int(data[0].get('totalvisitor'))
       updatedtotalvisitor=totalvisitor+1
       updatedata=Count.objects.get(id=1)
       updatedata.totalvisitor=updatedtotalvisitor
       updatedata.save()
      

       totalregisteruser=int(len(Customer.objects.all()))
       updaterigester=Count.objects.get(id=1)
       updaterigester.tatalregister=totalregisteruser
       updaterigester.save()

       totalpackage=int(len(Package.objects.all()))
       updatepackage=Count.objects.get(id=1)
       updaterigester.totalpackage=totalpackage
       updaterigester.save()

       fatch=Package.objects.all().order_by('-id')[:3]
       if fatch:
          contex={
                 "totalpackage":totalpackage,
                 "tatalregister":totalregisteruser,
                 "totalvisitor":updatedtotalvisitor,
                 "item":fatch
          }
          request.session['name']="ghelo"
          return render(request,'index.html' ,contex)
       else:
              return render(request,'index.html')
def about(request):
       return render(request,'about.html')

def contact(request):
       if request.method=='POST':
              name=request.POST.get('name')
              email=request.POST.get('email')
              message=request.POST.get('massage')
              clientkey=request.POST['g-recaptcha-response']
              secretkey='6Ldrj0MkAAAAABH016Obv_PagpFzfP2HOgOQ9v3v'
              cptchadata={
                     'secret':secretkey,
                     'response':clientkey
              }
              r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=cptchadata)
              response=json.loads(r.text)
              verify=response['success']
              if verify:
                  new=Contact()
                  new.FullName=name
                  new.Email=email
                  new.Message=message
                  new.save()
                  messages.error(request,"Your Response Submitted Succesfully")
              else:
                  messages.error(request,"Captcha Is Not Verify")
       return render(request,'contact.html')

def Page_404(request,exception):
    return render(request,'Page_404.html')
      
# def Page_4042(request):
#      print("heloo")
     