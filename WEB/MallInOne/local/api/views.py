#generic

from rest_framework import generics, mixins
from django.db.models import Q

from local.models import Local
from .serializers import LocalSerializer

class LocalAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = LocalSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    qs = Local.objects.all()
    query = self.request.GET.get("q")
    if query is not None:
      qs = qs.filter(Q(name__icontains=query)|Q(highlighted__icontains=query)).distinct()
    return qs

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

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