from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('payhelp', views.payhelp, name='Home'),
    path('denim', views.denim, name='Home')
]
