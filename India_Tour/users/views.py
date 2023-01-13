from django.shortcuts import render, HttpResponse, redirect
from users.models import Customer
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
import random

name=""
mail=""
passw=""
image=""
phone=""
otp2=""
otpr2=""
emailr=""
rpwd=""

def signup(request):
    request.session['id']=""
    request.session['emailotp']=0
    if request.method == 'POST':
        # Get The Request Data
        global name
        global mail
        global passw
        global image
        global phone
        global otp2
        name=request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        passw = request.POST.get('pass')
        cpass = request.POST.get('cpass')
        
        otp=random.randint(10000, 99999)
        otp2 = str(otp)
        print(otp2)

        #Fatch The File Name And It's Extension
        # imagename = image.name
        # ex = imagename.split('.')[1]
        # ex = ex.lower()
        # print(ex)

        # Save The Data To The DataBase
        if not Customer.objects.filter(email=mail):
            if passw == cpass:
                if len(passw) >= 8:
                        if len(phone) == 10:
                            
                            subject, from_email, to = 'hello', 'tour.india1414@gmail.com',mail
                            text_content = 'This is an important message.'
                            html_content = '<img src="https://png.pngtrepng-vector/20201214/ourmid/  pngtree-indian-republic-day-design-with-flag-an  vector-png-png-image_  2556755.jpg" alt="Th  Logo"> <br> Hi User <br style="color:red;">     Is Your One Time Password(OTP)<strong>'+otp2+ '<strong><br>Use For Craete The Account India_Tour'

                            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                            request.session['name']="gh"
                            return redirect('email')
                            
                        else:
                            messages.error(
                                request, 'Mobile Number Should Only Contain 10 Number')

                else:
                    messages.error(
                        request, 'Password Must 8 Character Long !!!!')
            else:
                messages.error(
                    request, 'Conferm Password And Password Is Not Match !!!!') 

        else:
            messages.error(request, 'Email Is Already Exist !!!!')
    return render(request, 'signup.html')


def login(request):
    request.session['emailotp']=0
    if request.method == 'POST':
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        data = Customer.objects.filter(email=email).values()
        print(data)
        if data:
            if data[0].get('password') == passwd:
                request.session['id'] = data[0].get('id')
                request.session['uname']=data[0].get('name')
                request.session['uemail']=data[0].get('email')
                return redirect('/')
            else:
                messages.error(request, 'Password Are Incorrect')
                return redirect("login")
        else:
            messages.error(request, 'User Does Not Exist !!!!')
            return redirect("login")
    if request.session['id']:
        messages.error(request,"Alredy Loged In")
        return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    request.session['id'] = ""
    request.session['logedin'] = ""
    return redirect('/')


def profile(request):
    if request.method == 'POST':
        updateid = request.session['id']
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        if len(mobile)==10:
             if request.FILES.get('image')==None:
                 member = Customer.objects.get(id=updateid)
                 member.name = name
                 member.mobile = mobile
                 member.save()
             else:
                image=request.FILES['image']
                imagename = image.name
                ex = imagename.split('.')[1]
                ex = ex.lower()
                # print(ex)
                if ex=='jpg' or ex=='jpeg' or ex=='png':
                    member = Customer.objects.get(id=updateid)
                    member.name = name
                    member.mobile = mobile
                    member.image=image
                    member.save()
                else:
                    messages.error(request, 'You Should Only Upload JPG,JPEG OR PNG File')
        else:
            messages.error(request, 'Mobile Number Should Only Contain 10 Number')

        # print(member)
        # print(name,mobile)
    id = request.session['id']
    if not id == "":
        id = request.session['id']
        data = Customer.objects.filter(id=id).values()
        context = {
            'image': data[0].get('image'),
            'name': data[0].get('name'),
            'email': data[0].get('email'),
            'mobile': data[0].get('mobile'),
            'css':"sjfhdsffj"

        }
        return render(request, 'profile.html', context)
    else:
        messages.error(request, 'Whithout Login Not Goes To This Page')
        return redirect('/')


def email(request):
    if not request.session['name'] =="ghelo":
      
      if request.method=="POST":
         rot=request.POST.get('enter')
         rotp=str(rot)
         print(otp2)
         print(rotp)
         if rotp == otp2:
             new=Customer()
             new.name=name
             new.mobile=phone
             new.email=mail
             new.password=passw
             new.save()
             return redirect('login')
         else:
             messages.error(request, 'Otp Are Incorrect')
       
      context={
         'email': mail
      }
      return render(request,'email.html',context)  
    else:
        request.session['emailotp'] = 1
        return redirect('/')

def reemail(request):
    context={
         'email': emailr
      }
    return render(request,'email.html',context)
    
def forget(request):
    global rpwd
    global emailr
    if request.method=="POST":
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        print(pwd,email)
        uemail=Customer.objects.filter(email=email).values()
        if not uemail:
            messages.error(request,"User Does Not Exist Please Enter Valid Email Address")
        else:
            emailr=email
            rpwd=pwd
            otpr=random.randint(10000, 99999)
            otpr2 = str(otpr)
            print(rpwd,emailr,otpr2)
            subject, from_email, to = 'hello', 'tour.india1414@gmail.com',emailr
            text_content = 'This is an important message.'
            html_content = '<img src="https://png.pngtrepng-vector/20201214/ourmid/  pngtree-indian-republic-day-design-with-flag-an  vector-png-png-image_  2556755.jpg" alt="Th  Logo"> <br> Hi User <br style="color:red;">     Is Your One Time Password(OTP)<strong>'+otpr2+ '<strong><br>Used To Reset The Password '
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            h=msg.send()
            if h:
                print("hello")
            else:
                messages.error(request,"Some Technical Issue On The Server To Send The Massage")
            
    return render(request,'Forgate.html')