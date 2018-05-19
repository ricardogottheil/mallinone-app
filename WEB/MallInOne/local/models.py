from __future__ import unicode_literals
from django.db import models
from pygments import highlight
#from product.models import Product
from mall.models import Mall

class Local(models.Model):
  id         = models.IntegerField(primary_key=True, default=0)
  name       = models.CharField(max_length=120)
  mall      = models.ForeignKey(Mall, related_name='%(class)s_Local', null=True)
  #product    = models.ManyToManyField(Product, related_name='%(class)s_Local')
  owner = models.ForeignKey('auth.User', related_name='%(class)s_Local', on_delete=models.CASCADE, default='')
  highlighted = models.TextField(default='', null=True, blank=True)
  image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='', null=True, blank=True)
  map_url = models.CharField(max_length=300, default='', null=True, blank=True)
  # latitude = models.IntegerField(default=0)
  # longitude = models.IntegerField(default=0)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering =('name',)