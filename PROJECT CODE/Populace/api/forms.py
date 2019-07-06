from django import forms,PasswordInput

class piazzaLoginForm(forms.Form):
    email = forms.forms.EmailField()
    password = CharField(widget=PasswordInput())
