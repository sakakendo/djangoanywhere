from django.urls import path 
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('fs_redirect', views.fs_redirect, name='fs_redirect'),
]
