from django.db import models
    
class Contact(models.Model):
    FullName=models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Message=models.CharField(max_length=250)
    
    def __str__(self):
        return self.FullName

