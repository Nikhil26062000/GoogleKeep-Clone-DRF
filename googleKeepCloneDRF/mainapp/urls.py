from django.contrib import admin
from django.urls import path
from mainapp.views import *

urlpatterns = [
    path("",Test.as_view()),
    path("fun",hello),
    
]