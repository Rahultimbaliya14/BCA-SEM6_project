from django.http import HttpResponse 
from django.shortcuts import render 

def index(request):
   id=request.session[id]
   print(id)
   return render(request,'index.html')

def devloper(request):
   return render(request,'Devloper.html')

def devloper2(request):
   return render(request,'Devloper2.html')

def devloper3(request):
   return render(request,'Devloper3.html')
   