from django.shortcuts import render,redirect
from piazza_api import Piazza
from .forms import piazzaLoginForm,googleLoginForm
from django.contrib.auth import authenticate, login, logout
import re
import queue

# Create your views here.
def home(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return redirect('home')
    return render(request,'api/index.html')

def user_logout(request):
    logout(request)
    return redirect('home')



def signup(request):
    return render(request,'api/signup.html')

def profile(request):
    p = Piazza()
    #if this is a POST request we need to process the form data
    if request.method =='POST':
        form_p = piazzaLoginForm(request.POST)
        form_g = googleLoginForm(request.POST)
        if 'piazza_p' in request.POST:

            print("piazza")
            if form_p.is_valid():
                p_email = form_p.cleaned_data['email']
                p_password = form_p.cleaned_data['password']
                p.user_login(p_email,p_password)
                # print(p.get_user_profile())
                dict = p.get_user_profile()
                class_names = queue.Queue(maxsize=20)
                class_code = []
                content_p = []
                po = []
                sub = []
                date = []
                for i in dict['all_classes']:
                    class_names.put(dict['all_classes'][i]['num'])
                    class_code.append(i)
                    print(class_code)
                    for code in class_code:
                        networks = p.network(code)
                        content_p = networks.iter_all_posts()
                        print(content_p)
                        for posts in content_p:
                            sub.append(posts['history'][0]['subject'])
                            date.append(posts['history'][0]['created'])
                            cleanr = re.compile('<.*?>')
                            cleantext = re.sub(cleanr, '', posts['history'][0]['content'])
                            po.append(cleantext)


                final = zip(sub,date,po)
                return render(request,'api/piazza.html',{'class':class_names,'contents':final})
            elif 'google_g' in request.POST:
                if form_g.is_valid():
                    print("goole")
                return redirect('home')

    else:
        # if a GET (or any other method) we'll create a blank form
        form_p = piazzaLoginForm()
        form_g = googleLoginForm()
    return render(request,'api/profile.html',{
    'piazzaform':form_p,
    'googleform':form_g
    })