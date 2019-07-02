from django.shortcuts import render
from piazza_api import Piazza
# Create your views here.
def home(request):
    return render(request,'api/index.html')

def signup(request):
    return render(request,'api/signup.html')

def profile(request):
    p = Piazza()
    p.user_login()
    return render(request,'api/profile.html')
