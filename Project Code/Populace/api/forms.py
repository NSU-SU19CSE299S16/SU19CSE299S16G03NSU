from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class piazzaLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label ='Password',widget=forms.PasswordInput(),max_length=20,required=True)


class googleLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),max_length=20)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
