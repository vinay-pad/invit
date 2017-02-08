from django.shortcuts import render
from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
