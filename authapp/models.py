# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Publickey(models.Model):

    user= models.CharField(max_length=32,unique=True)
    key = models.CharField(max_length=512)

class Challenge(models.Model):

    user = models.CharField(max_length=32,unique=True)
    challenge= models.CharField(max_length=512)
