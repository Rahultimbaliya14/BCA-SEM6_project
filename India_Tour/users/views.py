from django.shortcuts import render,HttpResponse,redirect
from users.models import Customer
from django.contrib import messages


def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        mail=request.POST.get('mail')
        passw=request.POST.get('pass')
        cpass=request.POST.get('cpass')
        if not Customer.objects.filter(email=mail):
            if passw==cpass:
                  new=Customer(
                      name=name,
                      mobile=phone,
                      email=mail,
                      password=passw
                      )
                  new.save()
            else:
                messages.error(request, 'Conferm Password And Password Is Not Match !!!!')

        else:
           messages.error(request, 'Email Is Already Exist !!!!')
    return render(request,'signup.html')




def login(request): 
    if request.method=='POST':
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        data=Customer.objects.filter(email=email,password=passwd).values()
        print(data)
        if data:
            if data[0].get('password')==passwd:
                 request.session['id']=data[0].get('id')
                 return redirect('/') 
            else:
                messages.error(request, 'Password Are Incorrect')      
        else:
             messages.error(request, 'User Does Not Exist !!!!')
    return render(request,'login.html   ')


def logout(request):
    del request.session['id']
    return redirect('/') 

def profile(request):
    return HttpResponse("This Is your Profile")