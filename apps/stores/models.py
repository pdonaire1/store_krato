# -*- coding: utf-8 -*-
"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from cities.models import City

class Store(models.Model):
    """
    Class created for stores
    """
    name = models.CharField(max_length=80)
    city = models.ForeignKey(City)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.id)


class UserStore(models.Model):
    """
    Class that show the relationship beetween user and stores 
    and citires
    """
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.store) + ' | ' + str(self.user)