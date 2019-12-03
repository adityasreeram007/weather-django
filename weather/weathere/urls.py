from django.conf.urls import url#,pth,include
from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    
    path('',views.index),
    path(r'login/',views.main1,name="main1"),
    path(r'main/',views.contact,name="contact"),
    path(r'register/',views.register,name="register"),
    path(r'logout/',views.logout,name='logout'),
    path(r'search/',views.search,name='search')
]
