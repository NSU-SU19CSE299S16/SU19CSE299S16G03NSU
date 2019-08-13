from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('google-class/',views.profile_g, name='profile_g'),
    path('piazza/',views.profile_p, name='profile_p'),
    # path('piazza/<pk>/',views.piazza_posts, name='piazza_posts'),
    path('logout/',views.user_logout,name='logout')
    ]
