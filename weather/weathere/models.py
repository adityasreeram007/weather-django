# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class logg(models.Model):
    user=models.CharField(max_length=100)
    passer=models.CharField(max_length=20)
class regg(models.Model):
    user=models.CharField(max_length=20)
    passer=models.CharField(max_length=20)
    confpasser=models.CharField(max_length=20)
    email=models.CharField(max_length=20)