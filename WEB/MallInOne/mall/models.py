# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from local.models import Local

# Create your models here.
class Mall(models.Model):
  name       = models.CharField(max_length=120)
  local      = models.ForeignKey(Local, null=True)

  def __str__(self):
    return self.name