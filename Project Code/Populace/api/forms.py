from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Associated_course

class piazzaLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label ='Password',widget=forms.PasswordInput(),max_length=20,required=True)


class googleLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),max_length=20)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = "",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email here'}))
    first_name = forms.CharField(label = "",max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name = forms.CharField(label = "",max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Username'})
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<small class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"

        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder':'Password'})
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = "<ul class='form-text text-muted small'><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder':'Confirm password'})
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = "<small class='form-text text-muted'>Enter same password as before</small>"

class Associated_courseForm(forms.ModelForm):
    course_name = forms.CharField(max_length=100)
    class Meta:
        model = Associated_course
        fields = ('course_name',)
