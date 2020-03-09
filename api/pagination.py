from rest_framework import pagination

class UserCollectionPagination(pagination.PageNumberPagination):       
    page_size = 100
