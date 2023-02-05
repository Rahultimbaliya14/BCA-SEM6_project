from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('pay',views.pay),
    # path('Page_notfound',views.Page_4042,name="Page_notfound"),
]
