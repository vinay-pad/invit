from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework import generics
from users.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

