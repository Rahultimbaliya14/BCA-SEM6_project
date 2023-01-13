from django.shortcuts import render,HttpResponse,redirect
from .models import Package


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

