# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from local.models import Local


# Create your models here.
class Product(models.Model):
  local              = models.ForeignKey(Local, null=True) 
  name               = models.CharField(max_length=120)
  reference          = models.CharField(max_length=120, null=True, blank=True)
  price              = models.CharField(max_length=120, null=True, blank=True)
  brand              = models.CharField(max_length=120, null=True, blank=True)
  characteristics    = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name