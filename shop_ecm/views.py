from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Product

from shop_ecm import serializers


# API get detail, update, delete
class ProductUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializers
    lookup_field = 'pid'


# API get list and create
class ProductListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializers
