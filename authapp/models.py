# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Publickey(models.Model):

    user= models.TextField()
    key = models.TextField()

class Challenge(models.Model):

    user = models.TextField()
    challenge= models.TextField()
