from django.urls import path, include

from .views import RestaurantnamesListView, RestaurantnamesDetailView, RestaurantListView, RestaurantDetailView, RestaurentFilterView, UserCollectionsCreateView, RestaurantCollectionsCreateView, RestaurantCollectionsListView, RestaurantCollectionsDestroyView, UserCollectionsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('names/<str:name>', RestaurantnamesListView.as_view()),
    path('names/<int:pk>', RestaurantnamesDetailView.as_view()),
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/<int:pk>', RestaurantDetailView.as_view()),
    path('restaurants/<str:day>/<str:query_time>', RestaurentFilterView.as_view()),
    path('collections/<int:user_id>', UserCollectionsCreateView.as_view()),
    path('collections/<int:user_id>/restaurants/<int:restaurant_id>', RestaurantCollectionsListView.as_view()),
    path('collections/<int:user_id>/<str:collection_name>', RestaurantCollectionsCreateView.as_view()),
    path('collections/delete/<int:user_id>/<str:collection_name>/restaurants/<int:restaurant_id>', RestaurantCollectionsDestroyView.as_view()),
    path('collections/create', UserCollectionsCreateView.as_view()),
    path('collections/add', RestaurantCollectionsCreateView.as_view()),
    path('collections/update/<int:pk>', UserCollectionsRetrieveUpdateDestroyAPIView.as_view()),
]
