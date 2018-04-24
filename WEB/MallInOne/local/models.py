# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from product.models import Product

# Create your models here.
class Local(models.Model):
  id         = models.IntegerField(primary_key=True, default=0)
  name       = models.CharField(max_length=120)
  product    = models.ManyToManyField(Product)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering =('name',)