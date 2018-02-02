"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls'))
]
