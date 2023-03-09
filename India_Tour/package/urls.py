from django.urls import path
from .import views


urlpatterns = [
    path('',views.service),
    path('/book',views.book),
    path('/hfkdfhksdkfksdfkdsfkjdsjfhsd',views.book2,name="book2"),
    path('/hfkdfhksdkfksdfkdsfkjdsjfhDFGKDFG',views.payment,name="pay"),
    path('/packageinfo',views.showpackage,name="packageinfo"),
    path('/package',views.package),
    path('/admindel',views.deletep),
    path('/handlerequest',views.handlerequest,name="handlerequest")
]