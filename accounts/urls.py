from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('',home,name="home"),
    path('register/',register_request,name="register"),
    path('login/',login_request,name="login"),
    path('logout/',logout_request,name="logout"),
    
]