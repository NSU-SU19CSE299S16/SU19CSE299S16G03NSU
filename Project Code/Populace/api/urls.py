from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('google-class/',views.profile_g, name='profile_g'),
    path('piazza/',views.profile_p, name='profile_p'),
    path('google-class/oauth2callback/', views.oauth2callback, name='oauth2callback'),
    path('logout/',views.user_logout,name='logout')
    ]
