from django.urls import path
from  winnerapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('',views.index,name='index')

]