from django.shortcuts import render, HttpResponse, redirect
from users.models import Customer,Count
from package.models import Book
from django.contrib import messages

import requests
import json
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
otpd2=""

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

        clientkey=request.POST['g-recaptcha-response']
        secretkey='6Ldrj0MkAAAAABH016Obv_PagpFzfP2HOgOQ9v3v'
        cptchadata={
                'secret':secretkey,
                'response':clientkey
              }
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=cptchadata)
        response=json.loads(r.text)
        verify=response['success']
        print(verify)
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
                            if verify:
                                 subject, from_email, to = 'Create Account', 'tour.india142@gmail.com',mail
                                 text_content = 'This is an important message.'
                                 html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="img"> <br> Hi '+name+' <br> Is Your One Time Password(OTP)<strong style="color:red;">'+otp2+ '</strong><br>Use For Craete The Account India_Tour'
     
                                 msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                                 msg.attach_alternative(html_content, "text/html")
                                 msg.send()
                                 request.session['name']="gh"
                                 return redirect('email')
                            else:
                                messages.error(request, 'Captcha Is Not Verify')
                            
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
        clientkey=request.POST['g-recaptcha-response']
        secretkey='6Ldrj0MkAAAAABH016Obv_PagpFzfP2HOgOQ9v3v'
        cptchadata={
                'secret':secretkey,
                'response':clientkey
              }
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=cptchadata)
        response=json.loads(r.text)
        verify=response['success']
        if verify:
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
        else:
            messages.error(request, 'Captcha Does Not Verify!!!!')
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
        datapac=Book.objects.filter(Useremail=request.session['uemail'])
        if datapac:
            context = {
            'image': data[0].get('image'),
            'name': data[0].get('name'),
            'email': data[0].get('email'),
            'mobile': data[0].get('mobile'),
            'packagedata':datapac
        }
            return render(request, 'profile.html', context)
        else:
         context = {
            'image': data[0].get('image'),
            'name': data[0].get('name'),
            'email': data[0].get('email'),
            'mobile': data[0].get('mobile'),
            

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
      return render(request,'emailr.html',context)  
    else:
        request.session['emailotp'] = 1
        return redirect('/')

def reemail(request):
    if request.method=="POST":
        rotp=request.POST.get('enter')
        
        if rotp==otpr2:
            fetch=Customer.objects.get(email=emailr)
            print(rpwd)
            fetch.password=rpwd
            fetch.save()
            messages.error(request,"Your Password Reset Successfully")
            return redirect('login')
        else:
            messages.error(request,"Incorrect OTP Plz Try Again")
    context={
         'email': emailr
      }
    return render(request,'emailr.html',context)
    
def forget(request):
    global rpwd
    global emailr
    global otpr2
    if request.method=="POST":
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        uemail=Customer.objects.filter(email=email).values()

        clientkey=request.POST['g-recaptcha-response']
        secretkey='6Ldrj0MkAAAAABH016Obv_PagpFzfP2HOgOQ9v3v'
        cptchadata={
                'secret':secretkey,
                'response':clientkey
              }
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=cptchadata)
        response=json.loads(r.text)
        verify=response['success']

        if not uemail:
            messages.error(request,"User Does Not Exist Please Enter Valid Email Address")
        else:
            if not len(pwd) < 8:
                if verify:
                      emailr=email
                      rpwd=pwd
                      otpr=random.randint(10000, 99999)
                      otpr2 = str(otpr)
                      print(rpwd,emailr,otpr2)
                      subject, from_email, to = 'Forget Password', 'tour.india142@gmail.com',emailr
                      text_content = 'This is an important message.'
                      html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="Img"> <br> Hi '+uemail[0].get('name')+' <br>   Is Your One Time Password(OTP) <strong style="color:red;">'+otpr2+ ' </strong>  Used To Reset The Password '
                      msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                      msg.attach_alternative(html_content, "text/html")
                      h=msg.send()
                      if h:
                          return redirect('emailr')
                      else:
                         messages.error(request,"Some Technical Issue On The Server To Send The Massage")
                else:
                    messages.error(request,"Captcha Is Not Verify")
            else:
                print("hello")
                messages.error(request,"Password Should Be 8 Character Long !!!!")

            
    return render(request,'Forgate.html')

def demail(request):
        global otpd2
        id = request.session['id']
        if not id == "":
            name= request.session['uname']
            semail=request.session['uemail']
            otpd=random.randint(10000, 99999)
            otpd2 = str(otpd)
            print(rpwd,emailr,otpr2)
            subject, from_email, to = 'Unregister Account', 'tour.india142@gmail.com',semail
            text_content = 'This is an important message.'
            html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="Img"> <br> Hi '+name+' <br>   Is Your One Time Password(OTP) <strong style="color:red;">'+otpd2+ ' </strong>  Used To Unregistered The The Account '
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            h=msg.send()
            if h:
                return redirect('checkdr')
            else:
                messages.error(request,"Some Technical Issue On The Server To Send The Massage")
        else:
            messages.error(request, 'Ristricted')
            return redirect('/')

def  checkdr(request):
    if request.method=="POST":
        dotp=request.POST.get('enter')
        if otpd2==dotp:
            new=Customer.objects.get(id=request.session['id'])
            new.delete()
            messages.error(request,"Account Unregistered Successfully")
            return redirect('logout')
        else:
            messages.error(request,"OTP Is Incorrect")
    
    
    
    id = request.session['id']
    if not id == "":
        context={
         'email': request.session['uemail']
        }
        return render(request,'emailr.html',context)
    else:
        messages.error(request, 'Ristricted')
        return redirect('/')