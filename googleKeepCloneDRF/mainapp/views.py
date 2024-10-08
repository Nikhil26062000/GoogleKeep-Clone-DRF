from tkinter.tix import CheckList
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from mainapp.serializers import *

"""
1. create a virual env
- python -m venv .venv

2. activate a virtual env
-(cmd) -> .venv\Scripts\activate
-(powershell) -> .venv\Scripts\Activate.ps1

3. inside .venv install django and djangorestframework

4. create a project using 
- "django-admin startproject myproject" command

5.cd myproject
python manage.py startapp api (this command is to create a new app)

6. Add DRF to Installed Apps

7.python manage.py migrate

8.python manage.py runserver

 
"""

# Create your views here.
@api_view()
def hello(request):
    return Response({'name':"nikhil"})

# This is view using class
class Test(APIView):
    def get(self, request,format=None):
        return Response({'name':'Nikhil Raj'})
    
    
class AllListAPIView(APIView):
    def get(self, request,format=None):
        data = CheckList.objects.all()
        serializer = AllListSerializer(data,many=True)
        serialized_data = serializer.data
        return Response(serialized_data)