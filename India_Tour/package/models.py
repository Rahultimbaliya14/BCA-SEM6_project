from django.db import models

class Package(models.Model):
    Title=models.CharField(max_length=225)
    Discription=models.CharField(max_length=500)
    DateOfStart=models.DateField(max_length=225)
    DateOfEnd=models.DateField(max_length=225)
    image=models.ImageField(upload_to='package/')

    def __str__(self):
        return self.Title

