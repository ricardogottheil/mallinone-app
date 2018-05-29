#generic

from rest_framework import generics, mixins

from product.models import Product
from .serializers import ProductSerializer

from django.db.models import Q

class ProductAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = ProductSerializer
  # queryset              = Product.objects.all()

  def get_queryset(self):
    qs = Product.objects.all()
    query = self.request.GET.get("q")
    if query is not None:
      qs = qs.filter(Q(name__icontains=query)|Q(highlighted__icontains=query)|Q(characteristics__icontains=query)).distinct()
    return qs

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = ProductSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    return Product.objects.all()

  # def get_object(self);
  #   pk = self.kwargs.get("pk")
  #   return Local.objects.get(pk=pk)