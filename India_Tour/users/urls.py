from django.urls import include
from .import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     path('/signup',views.signup,name='signup'),
     path('/login',views.login,name='login'),
     path('/logout',views.logout),
     path('/profile',views.profile),
     path('/forget',views.forget),
     path('/email',views.email,name='email'),
     path('/emailr',views.reemail,name='emailr'),

]