# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
  name      = models.CharField(max_length=120)
  reference = models.CharField(max_length=120, null=True, blank=True)
  precio    = models.CharField(max_length=120, null=True, blank=True)

  def __str__(self):
    return self.name