# -*- coding: utf-8 -*-
"""
Created by: @pdonaire1
Django settings for store_krato project.
"""
from __future__ import unicode_literals
from django.db import models

class City(models.Model):
    """
    Model Class for cities
    """
    name = models.CharField(max_length=80)

    def __str__(self):
        return "%s - %s" % (str(self.id), str(self.name))