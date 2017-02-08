from django.shortcuts import render
from rest_framework import generics
from membership.serializers import MembershipSerializer
from membership.models import Membership

class MembershipList(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

