from django.urls import path
from .import views


urlpatterns = [
    path('',views.service),
    path('/book',views.book),
    path('/package',views.package),
    path('/admindel',views.deletep)
]