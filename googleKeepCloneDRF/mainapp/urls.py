from django.contrib import admin
from django.urls import path
from mainapp.views import *

urlpatterns = [
    path("",hello),
    path("class",Test.as_view())
]