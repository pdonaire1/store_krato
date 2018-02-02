"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from rest_framework import routers
from stores.views_api_v1 import StoreViewSet

router = routers.SimpleRouter()
router.register(r'stores', StoreViewSet)
