from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestaurantSerializer, RestaurantnamesSerializer, UserCollectionsSerializer, RestaurantCollectionsSerializer
from .models import Restaurant, Restaurant_names, UserCollections, RestaurantCollections
from rest_framework.decorators import action
from datetime import datetime
from .pagination import UserCollectionPagination
# Create your views here.

class RestaurantnamesListView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        name = self.kwargs.get('name')
        queryset = Restaurant.objects.filter(restaurant__name__icontains=self.kwargs.get('name'))

        return queryset

    def get(self, request, *args, **kwargs):
        name = self.kwargs.get('name', None)
        if name is None:
            return Response({'error': 'No query name provided.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

class RestaurantnamesDetailView(generics.RetrieveDestroyAPIView):
    queryset = Restaurant_names.objects.all()
    serializer_class = RestaurantnamesSerializer

class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetailView(generics.RetrieveDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurentFilterView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        day = self.kwargs.get('day').lower()
        query_time = self.kwargs.get('query_time')

        if day == 'sunday':
            queryset = Restaurant.objects.filter(opening_time__sunday__lte=query_time, closing_time__sunday__gte=query_time)
        if day == 'monday':
            queryset = Restaurant.objects.filter(opening_time__monday__lte=query_time, closing_time__monday__gte=query_time)
        if day == 'tuesday':
            queryset = Restaurant.objects.filter(opening_time__tuesday__lte=query_time, closing_time__tuesday__gte=query_time)
        if day == 'wednesday':
            queryset = Restaurant.objects.filter(opening_time__wednesday__lte=query_time, closing_time__wednesday__gte=query_time)
        if day == 'thursday':
            queryset = Restaurant.objects.filter(opening_time__thursday__lte=query_time, closing_time__thursday__gte=query_time)
        if day == 'friday':
            queryset = Restaurant.objects.filter(opening_time__friday__lte=query_time, closing_time__friday__gte=query_time)
        if day == 'saturday':
            queryset = Restaurant.objects.filter(opening_time__saturday__lte=query_time, closing_time__saturday__gte=query_time)

        return queryset
    
    def get(self, request, *args, **kwargs):
        valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = self.kwargs.get('day').lower()

        if day not in valid_days:
            return Response({'error': 'Wrong day format. Please use one of "monday", "tuesday", "wednesday", "thursday", "friday", "saturday" or "sunday"'}, status=status.HTTP_400_BAD_REQUEST)
        query_time = self.kwargs.get('query_time', None)

        try:
            datetime.strptime(query_time,'%H:%M:%S')
        except ValueError:
            return Response({'error': 'Wrong time format. Please use valid 24hr format'}, status=status.HTTP_400_BAD_REQUEST)

        return super().get(request, *args, **kwargs)

class UserCollectionsCreateView(generics.ListCreateAPIView):
    serializer_class = UserCollectionsSerializer
    pagination_class = UserCollectionPagination

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = UserCollections.objects.filter(user__id=user_id)

        return queryset
    
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id', None)

        if user_id is None:
            return Response({'error': 'Please provide a user id.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().get(request, *args, **kwargs)

class RestaurantCollectionsCreateView(generics.ListCreateAPIView):
    serializer_class = RestaurantCollectionsSerializer
    pagination_class = UserCollectionPagination

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        collection_name = self.kwargs.get('collection_name')

        queryset = RestaurantCollections.objects.filter(restaurant_collection__user__id=user_id, restaurant_collection__name=collection_name)

        return queryset
    
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id', None)
        collection_name = self.kwargs.get('collection_name', None)

        if user_id is None:
            return Response({'error': 'Please provide a user id.'}, status=status.HTTP_400_BAD_REQUEST)
        if collection_name is None:
            return Response({'error': 'Please provide a collection name.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().get(request, *args, **kwargs)

class RestaurantCollectionsListView(generics.ListCreateAPIView):
    serializer_class = RestaurantCollectionsSerializer
    pagination_class = UserCollectionPagination

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        restaurant_id = self.kwargs.get('restaurant_id')

        queryset = RestaurantCollections.objects.filter(restaurant_collection__user__id=user_id, restaurant__id=restaurant_id)

        return queryset
    
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id', None)
        restaurant_id = self.kwargs.get('restaurant_id', None)

        if user_id is None:
            return Response({'error': 'Please provide a user id.'}, status=status.HTTP_400_BAD_REQUEST)
        if restaurant_id is None:
            return Response({'error': 'Please provide a restaurant id.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().get(request, *args, **kwargs)
