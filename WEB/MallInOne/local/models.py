from __future__ import unicode_literals
from django.db import models
from pygments import highlight
from product.models import Product

class Local(models.Model):
  id         = models.IntegerField(primary_key=True, default=0)
  name       = models.CharField(max_length=120)
  product    = models.ManyToManyField(Product, related_name='%(class)s_Local')
  owner = models.ForeignKey('auth.User', related_name='%(class)s_Local', on_delete=models.CASCADE, default='')
  highlighted = models.TextField(default='')
  image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='')
  latitude = models.IntegerField(default=0)
  longitude = models.IntegerField(default=0)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering =('name',)