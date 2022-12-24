from django.shortcuts import render,HttpResponse,redirect
from users.models import Customer
from django.contrib import messages




def signup(request):
    if request.method=='POST':
        #Get The Request Data
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        mail=request.POST.get('mail')
        passw=request.POST.get('pass')
        cpass=request.POST.get('cpass')
        image=request.FILES['image']

        #Fatch The File Name And It's Extension
        imagename=image.name
        ex=imagename.split('.')[1]
        ex=ex.lower()
        print(ex)

        #Save The Data To The DataBase
        if not Customer.objects.filter(email=mail):
            if passw==cpass:
                if len(passw)>=8:
                    if ex=="jpg" or ex=="png" or ex=="jpeg":
                        if len(phone)==10:
                             new=Customer(
                                 name=name,
                                 mobile=phone,
                                 email=mail,
                                 password=passw,
                                 image=image
                                 )
                             new.save()
                        else:
                            messages.error(request, 'Mobile Number Should Only Contain 10 Number')
       
                    else:
                        messages.error(request, 'Only Upload PNG,JPEG,JPG')
                else:
                    messages.error(request, 'Password Must 8 Character Long !!!!')
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
    if request.session['id']:
        request.session['logedin']=1
        return redirect('/')
    else:
        return render(request,'login.html')


def logout(request):
    request.session['id']=""
    request.session['logedin']=""
    return redirect('/') 

def profile(request):
    if request.method=='POST':
        updateid=request.session['id']
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        print(mobile)
        member = Customer.objects.get(id=updateid)
        member.name=name
        member.mobile=mobile
        member.save()
        # print(member)
        # print(name,mobile)
    id=request.session['id']
    if not id=="":
         id=request.session['id']
         data=Customer.objects.filter(id=id).values()
         context = {
         'image': data[0].get('image'),
         'name':data[0].get('name'),
         'email':data[0].get('email'),
         'mobile':data[0].get('mobile')
         }
         return render(request,'profile.html',context)
    else:
        messages.error(request, 'profile')
        return redirect('/')