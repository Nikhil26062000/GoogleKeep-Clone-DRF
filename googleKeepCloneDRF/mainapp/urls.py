from django.contrib import admin
from django.urls import path
from mainapp.views import *

urlpatterns = [
    path("",Test.as_view()),
    path("fun",hello),
    path("api/all/",AllListAPIView.as_view()),
    path("api/list/<int:pk>/",ListAPIView.as_view()),
    path("api/list-item/",CheckListItem_CreateAPIView.as_view()),
    path("api/list-item/all/",checkListItem_ALLAPIView.as_view()),
    path("api/list-item/<int:pk>/",CheckListItem_APIView.as_view())
    
]