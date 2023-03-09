from django.db import models

class Package(models.Model):
    Title=models.CharField(max_length=225)
    Discription=models.CharField(max_length=500)
    DateOfStart=models.DateField(max_length=225)
    Prise=models.CharField(max_length=225)
    Listofplace=models.CharField(max_length=225)
    Totalseet=models.CharField(max_length=225)
    image=models.ImageField(upload_to='package/')

    def __str__(self):
        return self.Title

class Book(models.Model):
    PaymentId=models.CharField(max_length=225)
    Packageid=models.CharField(max_length=225)
    Packagename=models.CharField(max_length=225)
    Username=models.CharField(max_length=225)
    Useremail=models.CharField(max_length=225)
    dateofbook=models.DateField(max_length=225)
    Totalamount=models.CharField(max_length=225)
    Totalperson=models.CharField(max_length=225)
    ConfermationNumber=models.CharField(max_length=225)

    def __str__(self):
        return self.Packagename
    
class Payment(models.Model):
    OrderId=models.CharField(max_length=225)
    Code=models.CharField(max_length=225)
    Bankname=models.CharField(max_length=225)
    Paymentmode=models.CharField(max_length=225)
    Amount=models.CharField(max_length=225)
    Status=models.CharField(max_length=225)
    Date=models.CharField(max_length=225)
    
    def __str__(self):
        return self.OrderId