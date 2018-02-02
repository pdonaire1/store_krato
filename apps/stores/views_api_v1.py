"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
import django_filters.rest_framework
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from stores.models import Store, UserStore
from stores.serializers import StoreSerializer, UserSerializer
from django.contrib.auth.models import User

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = [AllowAny, ]
    http_method_names = ['get']

    def get_queryset(self):
        return Store.objects.all()

    @detail_route(methods=['get'], permission_classes=[])
    def users(self, request, pk):
        """
        5.a. GET todos los usuarios de una tienda.
        """
        store = Store.objects.get(id=pk)
        user_store_ids = UserStore.objects.filter(store=store).values('user__id')
        users = User.objects.filter(id__in=user_store_ids)
        return Response(UserSerializer(users, many=True).data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = [AllowAny, ]
    http_method_names = ['get']

    @detail_route(methods=['get'], permission_classes=[])
    def stores(self, request, pk):
        """
        5.b. GET de todas las tiendas dado el id de un usuario.
        """
        user = User.objects.get(id=pk)
        user_store_ids = UserStore.objects.filter(user=user).values('store__id')
        stores = Store.objects.filter(id__in=user_store_ids)
        return Response(StoreSerializer(stores, many=True).data)