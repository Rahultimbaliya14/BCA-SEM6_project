from django.urls import include
from .import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     path('/signup',views.signup,name='signup'),
     path('/login',views.login),
     path('/logout',views.logout),
     path('/profile',views.profile),
]