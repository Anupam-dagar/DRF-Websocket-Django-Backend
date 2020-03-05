from django.urls import path, include

from .views import RestaurantnamesListView, RestaurantnamesDetailView, RestaurantListView, RestaurantDetailView

urlpatterns = [
    path('names/', RestaurantnamesListView.as_view()),
    path('names/<int:pk>', RestaurantnamesDetailView.as_view()),
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/<int:pk>', RestaurantDetailView.as_view()),
]
