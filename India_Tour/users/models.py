from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=250)
    mobile=models.CharField(max_length=40)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=20)
    image = models.ImageField(upload_to='user/')

    def __str__(self):
        return self.name