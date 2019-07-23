from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('piazza/',views.profile, name='piazza'),
    path('logout/',views.user_logout,name='logout')
    ]
