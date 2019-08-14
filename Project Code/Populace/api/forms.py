from django import forms

class piazzaLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label ='Password',widget=forms.PasswordInput(),max_length=20,required=True)

       
class googleLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),max_length=20)
