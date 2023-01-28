from django.shortcuts import render,HttpResponse,redirect
from .models import Package
from django.contrib import messages


# Create your views here.
def service(request):
    fatch=Package.objects.all().order_by('-id')
    print(fatch[0].Title)
    contex={
            "item":fatch
           }
    return render(request,'Packages.html',contex)

def book(request):
    if request.method=='POST':
        return HttpResponse("hello")
    else:
        return redirect('/')
def package(request):
    if request.method=="POST":
        id=request.POST.get('id')
        new=Package.objects.get(id=id)
        contex={
            'item':new 
        }
        return render(request,'Package.html',contex)
    else:    
        messages.error(request,"Plz Select The Package")
        return redirect('/services')

