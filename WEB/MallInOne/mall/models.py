from django.db import models
from pygments import highlight
from django.contrib.auth.models import User
#from local.models import Local

class Mall(models.Model):
  id         = models.IntegerField(primary_key=True, default=0)
  name       = models.CharField(max_length=120)
  owner = models.ForeignKey(
  	'auth.User', related_name='mall', on_delete=models.CASCADE, default='')
  highlighted = models.TextField(default='', null=True, blank=True)
  image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='', null=True, blank=True)
  map_url = models.CharField(max_length=300, default='', null=True, blank=True)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ('name',)