from .models import Restaurant, Restaurant_names, UserCollections
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
        fields = ('restaurant', 'opening_time', 'closing_time')

class UserCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCollections
        fields = ('name', 'user')

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(UserCollectionsSerializer, self).to_representation(instance)
