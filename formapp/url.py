from django.urls import path
from . import views
from .views import *

# from django.contrib import views
from .views import  index,home,contact


urlpatterns = [


    path('', index, name="index"),
    path('form',home,name="home"),
    path('contact',contact,name="contact"),
   
   
   
]