# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=16)
    u_password = models.CharField(max_length=16)
    u_sex = models.CharField(max_length=3)
    u_phonenum = models.CharField(max_length=13)
    u_birthday = models.DateField()
    u_location = models.CharField(max_length=16)
    u_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
