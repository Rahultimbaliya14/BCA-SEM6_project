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
        
        request.session['packageid']=id
        return redirect('book2')
    else:
        return redirect('/')

def book2(request):
    if request.method=="POST":
        username=request.POST['name']
        useremail=request.POST['email']
        TotalPerson=request.POST['Totalperson']
        packageid=request.POST['packageid']
        packagename=request.POST['packagename']
        packageamount=request.POST['packageamount']
        TotalPerson=int(TotalPerson)
        packageamount=int(packageamount)
        totalamount=packageamount*TotalPerson
        print(packageid)
        fatch=Package.objects.filter(id=packageid).values()
        availableseet=int(fatch[0].get('Totalseet'))
        if TotalPerson>availableseet:
            messages.error(request,"Only %d  Sheet left" %availableseet)
        else:
            print("hello")

    if not request.session['packageid']=="":
        data=Package.objects.get(id=request.session['packageid'])
        context={
            'item':data
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

