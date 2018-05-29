#generic

from rest_framework import generics

from product.models import Product
from .serializers import ProductSerializer

class ProductAPIView(generics.ListAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = ProductSerializer
  # queryset              = Product.objects.all()

  def get_queryset(self):
    return Product.objects.all()

class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = ProductSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    return Product.objects.all()

  # def get_object(self);
  #   pk = self.kwargs.get("pk")
  #   return Local.objects.get(pk=pk)