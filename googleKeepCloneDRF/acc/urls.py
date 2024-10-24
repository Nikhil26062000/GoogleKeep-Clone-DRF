from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)

from acc.views import *

urlpatterns = [
    # path for login
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
   
    # path for register
    path("api/register/",RegisterAPIView.as_view())
    
    
    
]