from __future__ import unicode_literals
from django.db import models
from pygments import highlight
from product.models import Product

# Create your models here.
class Local(models.Model):
  id         = models.IntegerField(primary_key=True, default=0)
  name       = models.CharField(max_length=120)
  product    = models.ManyToManyField(Product)
  owner = models.ForeignKey(
  	'auth.User', related_name='local', on_delete=models.CASCADE)
  highlighted = models.TextField()

  def __unicode__(self):
    return self.name

  class Meta:
    ordering =('name',)