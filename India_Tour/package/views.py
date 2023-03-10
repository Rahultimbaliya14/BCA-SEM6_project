from django.shortcuts import render,HttpResponse,redirect
from .models import Package,Book,Payment
from datetime import date
import random
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages
from Paytm import Checksum
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'bKMfNxPPf_QdZppa'

# Create your views here.
username=""
useremail=""
TotalPerson=""
packageid=""
packagename=""
totalamount=""
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
    id = request.session['id']
    if not id == "":
         if request.method=='POST':
             id=request.POST.get('id')
             
             request.session['packageid']=id
             return redirect('book2')   
         else:
             messages.error(request,"Package Is Not Selected")
             return redirect('/')
    else:
        messages.error(request,'login Please')
        return redirect('/')

def book2(request):
    global username
    global useremail
    global TotalPerson
    global packageid
    global packagename
    global totalamount

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
        request.session['amount']=totalamount
        print(packageid)
        fatch=Package.objects.filter(id=packageid).values()
        availableseet=int(fatch[0].get('Totalseet'))
        if TotalPerson>availableseet:
            messages.error(request,"Only %d  Sheet left" %availableseet)
        else:
           cont={
               "username":username,
               "packageamount":packageamount
           }
           return redirect('pay')

    if not request.session['packageid']=="":
        data=Package.objects.get(id=request.session['packageid'])
        context={
            'item':data
        } 
        return render(request,'Book.html',context)
    else:
        print("not hellods")
        return redirect('/')



def payment(request):
    if request.method=="POST":
        ordid=random.randint(1000000000,9999999999)
        orderid= str(ordid)
        #opt for paytm authentication 489871
        param_dict={
            'MID': 'DIY12386817555501617',
            'ORDER_ID':str(orderid),
            'TXN_AMOUNT':str(totalamount),
            'CUST_ID': useremail,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/services/handlerequest',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paymant2.html', {'param_dict': param_dict})
        # print("payment")
        # currentdate=date.today()
        # confermationnumber=random.randint(10000000000, 99999999999)
        # save=Book()
        # save.Packageid=packageid
        # save.Packagename=packagename
        # save.Username=username
        # save.Useremail=useremail
        # save.dateofbook=currentdate
        # save.Totalamount=totalamount
        # save.Totalperson=TotalPerson
        # save.ConfermationNumber=confermationnumber
        # save.save()
        # upa=Package.objects.filter(id=packageid).values()
        # total=upa[0].get('Totalseet')
        # print(total)
        # confo=str(confermationnumber)
        # subject, from_email, to = 'Package Is Succesfully Booked', 'zoomanagmentsystem@gmail.com',useremail
        # text_content = 'This is an important message.'
        # html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="Img"> <br> Hi '+username+' <br>  Your Package  Is Successfully Booked With Confermation Number <strong style="color:red;">'+confo+ ' </strong>  Save This Confermation Number To Further Comunication'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # h=msg.send()
        # messages.success(request,"Your Package Is Successfully Booked With Confermatiomn Number %s Please Check Your Email " %confo)
        # return redirect('/')
    if not request.session['packageid']=="":
       return render(request,'payment.html')
    else:
        messages.error(request,"This Is The Payment Page You Not Directly In")
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
    print('del')
    data=Package.objects.all().values()
    for d in data:
        dater=d['DateOfStart']
        current=date.today()
        if current>dater:
            deletepakage=Package.objects.get(id=d['id'])
            deletepakage.delete()
    return redirect("/")

def showpackage(request):
    if request.method=="POST":
        data=Book.objects.get(id=request.POST.get('id'))
        data2=Book.objects.filter(id=request.POST.get('id')).values()
        # print(data2[0].get('Packageid'))
        # print(data)
        data3=Package.objects.filter(id=data2[0].get('Packageid')).values()
        # print(data3[0].get('image'))
        context={
            'image':data3[0].get('image'),
            'item':data
        }
        return render(request,'packageinfo.html',context)
    else:
        messages.error(request,"Please Select The Package That You Book")
        return redirect('/acount/profile')

@csrf_exempt
def handlerequest(request):
    if request.method=="POST":
        status=request.POST.get('RESPCODE')
        if status=='01':
            orderid=request.POST.get('ORDERID')
            pay=Payment()
            pay.OrderId=(request.POST.get('ORDERID'))
            pay.Bankname=(request.POST.get('BANKNAME'))
            pay.Amount=(request.POST.get('TXNAMOUNT'))
            pay.Code=(request.POST.get('RESPCODE'))
            pay.Date=(request.POST.get('TXNDATE'))
            pay.Paymentmode=(request.POST.get('PAYMENTMODE'))
            pay.Status=(request.POST.get('STATUS'))
            pay.save()
        # print(request.POST.get('RESPCODE'))
        # print(request.POST.get('RESPMSG'))
        # print(request.POST.get('BANKNAME'))
        # print(request.POST.get('PAYMENTMODE'))
        # print(request.POST.get('TXNAMOUNT'))
        # print(request.POST.get('ORDERID'))
        # print(request.POST.get('STATUS'))
        # print(request.POST.get('TXNDATE'))
        
            currentdate=date.today()
            confermationnumber=random.randint(10000000000, 99999999999)
            save=Book()
            save.Packageid=packageid
            save.Packagename=packagename
            save.Username=username
            save.Useremail=useremail
            save.dateofbook=currentdate
            save.PaymentId=orderid
            save.Totalamount=totalamount
            save.Totalperson=TotalPerson
            save.ConfermationNumber=confermationnumber
            save.save()
            upa=Package.objects.filter(id=packageid).values()
            total=upa[0].get('Totalseet')
            print(total)
            confo=str(confermationnumber)
            subject, from_email, to = 'Package Is Succesfully Booked', 'zoomanagmentsystem@gmail.com',useremail
            text_content = 'This is an important message.'
            html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="Img"> <br> Hi '+username+' <br>  Your Package  Is Successfully Booked With Confermation Number <strong style="color:red;">'+confo+ ' </strong>  Save This Confermation Number To Further Comunication'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            h=msg.send()
            messages.success(request,"Your Package Is Successfully Booked With Confermatiomn Number %s Please Check Your Email " %confo)
            return redirect('/')  
        else:
            # print(request)
            # return HttpResponse(request)
            # pay.OrderId=(request.POST.get('ORDERID'))
            orderid=request.POST.get('ORDERID')
            currentdate=date.today()
            confermationnumber=random.randint(10000000000, 99999999999)
            save=Book()
            save.Packageid=packageid
            save.Packagename=packagename
            save.Username=username
            save.Useremail=useremail
            save.dateofbook=currentdate
            save.PaymentId=orderid
            save.Totalamount=totalamount
            save.Totalperson=TotalPerson
            save.ConfermationNumber=confermationnumber
            save.save()
            upa=Package.objects.filter(id=packageid).values()
            total=upa[0].get('Totalseet')
            print(total)
            confo=str(confermationnumber)
            subject, from_email, to = 'Package Is Succesfully Booked', 'zoomanagmentsystem@gmail.com',useremail
            text_content = 'This is an important message.'
            html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="Img"> <br> Hi '+username+' <br>  Your Package  Is Successfully Booked With Confermation Number <strong style="color:red;">'+confo+ ' </strong>  Save This Confermation Number To Further Comunication'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            h=msg.send()
            messages.success(request,"Your Package Is Successfully Booked With Confermatiomn Number %s Please Check Your Email " %confo)
            return redirect('/')  
       
    else:
        messages.error(request,"Restricted")
        return redirect('/')