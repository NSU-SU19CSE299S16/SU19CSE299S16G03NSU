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
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
