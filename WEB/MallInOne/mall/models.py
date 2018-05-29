from django.db import models
from pygments import highlight
from django.contrib.auth.models import User
from django.conf import settings

class Mall(models.Model):
  name       = models.CharField(max_length=120)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  highlighted = models.TextField(default='', null=True, blank=True)
  image = models.CharField(max_length=300, default='', null=True, blank=True)
  map_url = models.CharField(max_length=300, default='', null=True, blank=True)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ('name',)