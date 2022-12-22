from django.http import HttpResponse 
from django.shortcuts import render 

def index(request):
   id=request.session[id]
   print(id)
   return render(request,'index.html')


