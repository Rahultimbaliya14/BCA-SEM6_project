from django.shortcuts import render,HttpResponse,redirect
from .models import Package
from datetime import date
from django.contrib import messages


# Create your views here.
def service(request):
    fatch=Package.objects.all().order_by('-id')
    if fatch:
        contex={
                "item":fatch
               }
        return render(request,'Packages.html',contex)
    else:
        return render(request,'Packages.html')

def book(request):
    if request.method=='POST':
        id=request.POST.get('id')
        print(id)
        data=Package.objects.filter(id=id).values()
        print(data)
        context={
            "item":data[0]
        }
        return render(request,'Book.html',context)
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

def deletep(request):
    
    data=Package.objects.all().values()
    for d in data:
        dater=d['DateOfStart']
        current=date.today()
        if current>dater:
            deletepakage=Package.objects.get(id=d['id'])
            deletepakage.delete()
    return redirect("/")

