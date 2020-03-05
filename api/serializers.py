from .models import Restaurant, Restaurant_names
from rest_framework import serializers


class RestaurantnamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_names
        fields = ('name',)

class RestaurantSerializer(serializers.ModelSerializer):
    restaurant = RestaurantnamesSerializer(many=False, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('restaurant', 'opening_time', 'closing_time', 'day')
