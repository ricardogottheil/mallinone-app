# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Local(models.Model):
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name