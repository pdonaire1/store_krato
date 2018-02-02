"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from django.conf.urls import url, include
from django.contrib import admin
from .api_router import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls'))
    url(r'^api/v1/', include(router.urls)),
]
