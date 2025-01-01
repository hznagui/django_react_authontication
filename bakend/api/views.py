from django.shortcuts import render

#heaeder that was adding 
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerialazers
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialazers
    permission_classes = [AllowAny]
