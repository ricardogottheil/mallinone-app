from __future__ import unicode_literals
from django.db import models
from pygments import highlight
from local.models import Local
from django.conf import settings

# Create your models here.
class Product(models.Model):
  local              = models.ForeignKey(Local, related_name='%(class)s_Product', null=True)
  name               = models.CharField(max_length=120)
  price              = models.CharField(max_length=120, null=True, blank=True)
  brand              = models.CharField(max_length=120, null=True, blank=True)
  characteristics    = models.TextField(null=True, blank=True)
  owner              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  highlighted        = models.TextField(default='', blank=True)
  image              = models.CharField(max_length=300, default='', null=True, blank=True)

  def __unicode__(self):
    return self.name

  class Meta:
  	ordering =('name',)