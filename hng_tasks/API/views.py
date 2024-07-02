from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import user_logged_in
from django.utils import timezone

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *
from .helpers import *


class Stage1_TaskView(APIView):
    def get(self, request, *args, **kwargs):
        
        ip = get_client_ip(request)
        
        response = {
            "client_ip": ip, #Ip address of the requester
            "location": get_location(ip), #city of the requester
            "greeting": "Hello User, the temperature is 11 degrees in New York"
        }
        
        return Response(get_location(ip), status=status.HTTP_200_OK)
# Create your views here.
