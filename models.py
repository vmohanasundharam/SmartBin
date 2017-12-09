# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class bin_info(models.Model):
    bin_id = models.CharField(max_length=100,primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    access_key = models.CharField(max_length=10)
    land_mark = models.CharField(max_length=20)
    current_level = models.FloatField(default=0)

class fill_level_stats(models.Model):
	bin_id =  models.CharField(max_length=100,primary_key=True)
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	bin_level = models.FloatField()


