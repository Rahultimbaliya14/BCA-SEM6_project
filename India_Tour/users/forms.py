from django import forms
from .models import *
 
 
class UserImage(forms.ModelForm):
 
    class Meta:
        model = Customer
        fields = ['image']