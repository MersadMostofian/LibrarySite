from django import forms
from django.contrib.auth.models import User

class userRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)