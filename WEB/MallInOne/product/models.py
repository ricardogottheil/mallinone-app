from __future__ import unicode_literals
from django.db import models
from pygments import highlight


# Create your models here.
class Product(models.Model):
  id                 = models.IntegerField(primary_key=True, default=0)
  name               = models.CharField(max_length=120)
  price              = models.CharField(max_length=120, null=True, blank=True)
  brand              = models.CharField(max_length=120, null=True, blank=True)
  characteristics    = models.TextField(null=True, blank=True)
  owner              = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
  highlighted        = models.TextField()

  def __unicode__(self):
    return self.name