from django.contrib import admin
from .models import Restaurant, Restaurant_names, RestaurantCollections, UserCollections
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Restaurant_names)
admin.site.register(RestaurantCollections)
admin.site.register(UserCollections)
