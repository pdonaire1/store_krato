"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from rest_framework import serializers
from stores.models import Store
from django.contrib.auth.models import User

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')