from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestaurantSerializer, RestaurantnamesSerializer
from .models import Restaurant, Restaurant_names
from rest_framework.decorators import action
# Create your views here.

class RestaurantnamesListView(generics.ListCreateAPIView):
    queryset = Restaurant_names.objects.all()
    serializer_class = RestaurantnamesSerializer

class RestaurantnamesDetailView(generics.RetrieveDestroyAPIView):
    queryset = Restaurant_names.objects.all()
    serializer_class = RestaurantnamesSerializer

class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetailView(generics.RetrieveDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer