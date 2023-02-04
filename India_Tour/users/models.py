from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=250)
    mobile=models.CharField(max_length=40)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=20)
    image = models.ImageField(upload_to='user/')

    def __str__(self):
        return self.name

class Count(models.Model):
    totalvisitor=models.CharField(max_length=255)
    tatalregister=models.CharField(max_length=225)
    totalpackage=models.CharField(max_length=225)


        