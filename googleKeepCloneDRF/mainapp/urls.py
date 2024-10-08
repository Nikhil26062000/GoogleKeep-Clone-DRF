from django.contrib import admin
from django.urls import path
from mainapp.views import *

urlpatterns = [
    path("",Test.as_view()),
    path("fun",hello),
    path("api/all",AllListAPIView.as_view()),
    path("api/list/<int:pk>/",ListAPIView.as_view())
    
]