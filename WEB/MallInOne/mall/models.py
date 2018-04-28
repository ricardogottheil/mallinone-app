from django.db import models
from pygments import highlight
from django.contrib.auth.models import User
from local.models import Local

class Mall(models.Model):
  name       = models.CharField(max_length=120)
  local      = models.ForeignKey(Local, related_name='%(class)s_Mall')#parent_link=True
  owner = models.ForeignKey(
  	'auth.User', related_name='mall', on_delete=models.CASCADE, default='')
  highlighted = models.TextField(default='')

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ('name',)