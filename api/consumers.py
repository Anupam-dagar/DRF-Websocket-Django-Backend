from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import UserCollections, RestaurantCollections, Restaurant
from .serializers import UserCollectionsSerializer, RestaurantCollectionsSerializer


class CollectionConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['collection_id']
        self.room_group_name = 'collection_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action_type = text_data_json['actiontype']
        message = text_data_json['message']
        
        if action_type == 'WEBSOCKET_EDIT_MESSAGE':
            collection_name = message['name']
            collection_id = message['id']
            
            try:
                UserCollections.objects.filter(id=collection_id).update(name=collection_name)
                return_data = UserCollectionsSerializer(UserCollections.objects.get(id=collection_id)).data
                action_type = 'SUCCESS_UPDATE_COLLECTION'
            except:
                return_data = {'error': 'Error editing collection name.'}
                action_type = 'FAILURE_UPDATE_COLLECTION'
        
        if action_type == 'WEBSOCKET_ADD_MESSAGE':
            collection_id = message['collectionId']
            restaurant_id = message['restaurantId']
            try:
                user_collection = UserCollections.objects.get(id=collection_id)
                restaurant = Restaurant.objects.get(id=restaurant_id)
                restaurant_object = RestaurantCollections(restaurant_collection=user_collection, restaurant=restaurant)
                restaurant_object.save()
                return_data = RestaurantCollectionsSerializer(restaurant_object).data
                action_type = 'SUCCESS_ADD_RESTAURANT_TO_COLLECTION'
            except:
                return_data = {'error': 'Error adding restaurant to collection.'}
                action_type = 'FAILURE_ADD_RESTAURANT_TO_COLLECTION'
        
        if action_type == 'WEBSOCKET_REMOVE_MESSAGE':
            user_id = message['user']
            collection_name = message['collectionName']
            restaurant_id = message['restaurantId']

            try:
                restaurant_object = RestaurantCollections.objects.get(restaurant_collection__collaborators__id=user_id, restaurant_collection__name=collection_name, restaurant__id=restaurant_id)
                restaurant_object.delete()
                restaurants = RestaurantCollections.objects.filter(restaurant_collection__collaborators__id=user_id, restaurant_collection__name=collection_name)
                restaurants_data = RestaurantCollectionsSerializer(restaurants, many=True).data
                return_data = {'success': {'success': collection_name}, 'restaurants': restaurants_data }
                action_type = 'SUCCESS_DELETE_RESTAURANTS_IN_COLLECTION'
            except:
                return_data = {'error': 'Error removing restaurant from collection.'}
                action_type = 'FAILURE_DELETE_RESTAURANTS_IN_COLLECTION'

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'collection_message',
                'message': return_data,
                'actiontype': action_type
            }
        )

    def collection_message(self, event):
        message = event['message']
        action_type = event['actiontype']

        self.send(text_data=json.dumps({
            'message': message,
            'actiontype': action_type
        }))
