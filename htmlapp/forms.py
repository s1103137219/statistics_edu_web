# -*- coding: UTF-8 -*-     
from django import forms

from django.contrib import auth

class loginform(forms.Form):
    
    email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'帳號','id':'id'}));
    passd =forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'密碼','id':'passd'}));
    date = forms.DateField()
    
class photoForm(forms.Form):
    image = forms.ImageField(required=False)

class Introduction(forms.Form):
        sef =forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))