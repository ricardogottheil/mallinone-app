#generic

from rest_framework import generics

from mall.models import Mall
from .serializers import MallSerializer

class MallAPIView(generics.ListAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = MallSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    return Mall.objects.all()

  # def perform_create(self, serializer):
  #   serializer.save(owner=self.request.user)

class MallRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = MallSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    return Mall.objects.all()

  # def get_object(self);
  #   pk = self.kwargs.get("pk")
  #   return Local.objects.get(pk=pk)