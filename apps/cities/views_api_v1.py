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
from cities.models import City
from stores.models import UserStore, Store
from django.contrib.auth.models import User
from cities.serializers import CitySerializer
from stores.serializers import StoreSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = [AllowAny, ]
    http_method_names = ['get']

    @detail_route(methods=['get'], permission_classes=[])
    def stores(self, request, pk):
        """
		5.c. GET de todas las tiendas de una ciudad, ASOCIADAS A UN USUARIO.
		@params: 
			@GET: user_id
		"""
        user_id = self.request.GET.get('user_id')
        if not user_id:
            return Response({'message': 'user_id is a required field'})
        city = City.objects.get(id=pk)
        user_store_ids = UserStore.objects.filter(user__id=user_id).values('store__id')
        stores = Store.objects.filter(
        	city=city,
        	id__in=user_store_ids
        	)
        return Response(StoreSerializer(stores, many=True).data)
