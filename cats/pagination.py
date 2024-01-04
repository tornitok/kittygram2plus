# cats/pagination.py
from requests import Response
from rest_framework.pagination import PageNumberPagination


class CatsPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'results': data
        })
