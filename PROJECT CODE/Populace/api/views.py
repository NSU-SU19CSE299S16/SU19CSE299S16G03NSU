from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'api/index.html')

def signup(request):
    return render(request,'api/signup.html')
