"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from rest_framework import routers
from stores.views_api_v1 import StoreViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'stores', StoreViewSet)
router.register(r'users', UserViewSet)

