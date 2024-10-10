from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from mainapp.serializers import *
from rest_framework import status
from mainapp.models import CheckList,CheckListItem
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view()
def hello(request):
    return Response({'name': "nikhil"})

# This is a view using class
class Test(APIView):
    def get(self, request):
        return Response({'name': 'Nikhil Raj'}) 

    
class AllListAPIView(APIView):
    serializer_class = AllListSerializer
    
    def get(self, request):
        data = CheckList.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
    
    # API for Post Request
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ListAPIView(APIView):
    serializer_class = AllListSerializer
    
    def get_obj(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404
    
    # API to get single data
    def get(self, request, pk):
        data = self.get_obj(pk)
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # API to update data
    def put(self, request, pk):
        data = self.get_obj(pk)
        serializer = self.serializer_class(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # API to delete data
    def delete(self, request, pk):
        data = self.get_obj(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class CheckListItem_CreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    # Api for Post request
    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class CheckListItem_APIView(APIView):
    serializer_class = CheckListItemSerializer
    
    def get_obj(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404
    
    # API to get single data
    def get(self, request, pk):
        data = self.get_obj(pk)
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # API to update data
    def put(self, request, pk):
        data = self.get_obj(pk)
        serializer = self.serializer_class(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # API to delete data
    def delete(self, request, pk):
        data = self.get_obj(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class checkListItem_ALLAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_obj(self):
        try:
            return CheckListItem.objects.all()
        except CheckListItem.DoesNotExist:
            raise Http404
    
    # Api to get all data   
    def get(self,request,format=None):
        data = self.get_obj()
        serializer = self.serializer_class(data,many=True)
        serialized_data = serializer.data
        return Response(serialized_data)