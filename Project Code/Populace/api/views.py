from django.shortcuts import render,redirect
from piazza_api import Piazza
from .forms import piazzaLoginForm,googleLoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import re
import queue
#google Classroom
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from django.urls import resolve
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'



SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
some = ''
def random_string(length=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(length))
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
    form_p = piazzaLoginForm()
    return render(request,'api/profile.html', {
    'piazzaform':form_p
    })


# Function for piazza api functionality and login
def profile_p(request):
    p = Piazza()
    #if this is a POST request we need to process the form data
    if request.method =='POST':
        form_p = piazzaLoginForm(request.POST)
        # form_g = googleLoginForm(request.POST)
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

    else:
        # if a GET (or any other method) we'll create a blank form
        form_p = piazzaLoginForm()
        # form_g = googleLoginForm()
        return render(request,'api/profile.html',{
        'piazzaform':form_p
        })


# Function for piazza api functionality and login
def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

def profile_g(request):
    if request.method =='POST':
        if 'credentials' not in request.session:


            flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            'client_secret.json', scopes=SCOPES)

            flow.redirect_uri = 'http://localhost:8000/google-class/oauth2callback/'

            authorization_url, state = flow.authorization_url(
            access_type='offline',
            prompt='consent',
            include_granted_scopes='true')

            request.session['state'] = state
            some = state
            print("/n" + "The state is =" + state + "/n")
            return redirect(authorization_url)
    else:
        return render(request,'api/profile.html')

def oauth2callback(request):
    state = request.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'client_secret.json', scopes=SCOPES, state=state)

    flow.redirect_uri = 'http://localhost:8000/google-class/oauth2callback/'
    authorization_response = request.get_full_path()
    # print(request.get_full_path())
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    request.session['credentials'] = credentials_to_d
    ict(credentials)

    if 'credentials' in request.session:
        # Load credentials from the session.
        credentials = google.oauth2.credentials.Credentials(
        request.session['credentials'])

        service = build(API_SERVICE_NAME,API_VERSION, credentials=credentials)

        # Call the Classroom API
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
        else:
            print('Courses:')
            for course in courses:
                print(course['name'])

    return render(request,'api/google-class.html')
