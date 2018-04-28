from __future__ import unicode_literals
from django.db import models
from pygments import highlight
from product.models import Product
#from mall.models import Mall

# Create your models here.
class Local(models.Model):
  id         = models.IntegerField(primary_key=True, default=0)
  name       = models.CharField(max_length=120)
  product    = models.ManyToManyField(Product, related_name='%(class)s_Local')
  owner = models.ForeignKey('auth.User', related_name='%(class)s_Local', on_delete=models.CASCADE, default='')
  highlighted = models.TextField(default='')

  def __unicode__(self):
    return self.name

  class Meta:
    ordering =('name',)