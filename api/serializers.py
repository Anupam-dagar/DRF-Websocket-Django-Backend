from .models import Restaurant, Restaurant_names, UserCollections, RestaurantCollections
from appauth.serializers import UserSerializer
from rest_framework import serializers


class RestaurantnamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_names
        fields = ('name',)

class RestaurantSerializer(serializers.ModelSerializer):
    restaurant = RestaurantnamesSerializer(many=False, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'restaurant', 'opening_time', 'closing_time')

class UserCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCollections
        fields = ('id', 'name', 'user', 'collaborators')

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        self.fields['collaborators'] = UserSerializer(read_only=True, many=True)
        return super(UserCollectionsSerializer, self).to_representation(instance)

class RestaurantCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCollections
        fields = ('id', 'restaurant_collection', 'restaurant')

    def to_representation(self, instance):
        self.fields['restaurant_collection'] =  UserCollectionsSerializer(read_only=True)
        self.fields['restaurant'] =  RestaurantSerializer(read_only=True)
        return super(RestaurantCollectionsSerializer, self).to_representation(instance)
