from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=250)
    mobile=models.IntegerField(max_length=30)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name