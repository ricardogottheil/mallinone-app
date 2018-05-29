from __future__ import unicode_literals
from django.db import models
from pygments import highlight
from mall.models import Mall
from django.conf import settings

class Local(models.Model):
  name       = models.CharField(max_length=120)
  mall      = models.ForeignKey(Mall, related_name='%(class)s_Local', null=True)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  highlighted = models.TextField(default='', null=True, blank=True)
  image = models.CharField(max_length=300, default='', null=True, blank=True)
  map_url = models.CharField(max_length=300, default='', null=True, blank=True)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering =('name',)
