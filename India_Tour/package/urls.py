from django.urls import path
from .import views


urlpatterns = [
    path('',views.service),
    path('/book',views.book),
    path('/book2',views.book2,name="book2"),
    path('/package',views.package),
    path('/admindel',views.deletep)
]