from django.urls import path, include

from .views import RestaurantnamesListView, RestaurantnamesDetailView, RestaurantListView, RestaurantDetailView, RestaurentFilterView, UserCollectionsCreateView

urlpatterns = [
    path('names/<str:name>', RestaurantnamesListView.as_view()),
    path('names/<int:pk>', RestaurantnamesDetailView.as_view()),
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/<int:pk>', RestaurantDetailView.as_view()),
    path('restaurants/<str:day>/<str:query_time>', RestaurentFilterView.as_view()),
    path('collections/create', UserCollectionsCreateView.as_view())
]
