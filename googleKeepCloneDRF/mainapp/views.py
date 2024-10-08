from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from mainapp.serializers import *
from rest_framework import status
from mainapp.models import CheckList  # Correct import

# Create your views here.
@api_view()
def hello(request):
    return Response({'name': "nikhil"})

# This is view using class
class Test(APIView):
    def get(self, request, format=None):
        return Response({'name': 'Nikhil Raj'})

    
class AllListAPIView(APIView):
    serializer_class = AllListSerializer
    
    def get(self, request, format=None):
        data = CheckList.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
    
    # API for Post Request
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ListAPIView(APIView):
    serializer_class = AllListSerializer
    
    def get(self, request, pk, format=None):
        data = CheckList.objects.get(pk=pk)
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
