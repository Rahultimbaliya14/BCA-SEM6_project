from django.urls import path
from .import views


urlpatterns = [
    path('',views.service),
    path('/book',views.book)
]