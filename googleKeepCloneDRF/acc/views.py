from django.shortcuts import render
from rest_framework.views import APIView
from acc.serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.
class  RegisterAPIView(APIView):
    serializer_class = UserregisterSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            res= {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                "user":serializer.data
                
            }
            

            return Response(res)
        return Response(serializer.errors)