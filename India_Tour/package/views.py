from django.shortcuts import render,HttpResponse
from .models import Package


# Create your views here.
def service(request):
    fatch=Package.objects.all().order_by('-id')
    print(fatch[0].Title)
    contex={
            "item":fatch
           }
    return render(request,'Packages.html',contex)
