from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('',show_about_page),
]