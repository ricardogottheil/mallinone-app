from django.db import models
from pygments import highlight

from local.models import Local

# Create your models here.
class Mall(models.Model):
  name       = models.CharField(max_length=120)
  local      = models.ForeignKey(Local)
  owner = models.ForeignKey(
  	'auth.User', related_name='mall', on_delete=models.CASCADE)
  highlighted = models.TextField()

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ('name',)