#generic

from rest_framework import generics

from local.models import Local
from .serializers import LocalSerializer

class LocalAPIView(generics.ListAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = LocalSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    return Local.objects.all()

  # def perform_create(self, serializer):
  #   serializer.save(owner=self.request.owner)

class LocalRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = LocalSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    return Local.objects.all()

  # def get_object(self);
  #   pk = self.kwargs.get("pk")
  #   return Local.objects.get(pk=pk)