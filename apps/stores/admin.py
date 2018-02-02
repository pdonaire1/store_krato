# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from stores.models import Store, UserStore
from cities.models import City

admin.site.register(City)
admin.site.register(Store)
admin.site.register(UserStore)