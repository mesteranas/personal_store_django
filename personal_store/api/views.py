from django.shortcuts import render
from home import models
from . import serializers
from rest_framework import generics,status
# Create your views here.
class viewItems(generics.ListCreateAPIView):
    queryset = models.item.objects.all()
    serializer_class = serializers.items
class getItems(generics.RetrieveDestroyAPIView):
    queryset = models.item.objects.all()
    serializer_class = serializers.items