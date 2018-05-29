#generic

from rest_framework import generics, mixins

from mall.models import Mall
from .serializers import MallSerializer

from django.db.models import Q

class MallAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  lookup_field          = 'pk' #slug, id # (r'(?P<pk>\d+)')
  serializer_class      = MallSerializer
  # queryset              = Local.objects.all()

  def get_queryset(self):
    qs = Mall.objects.all()
    query = self.request.GET.get("q")
    if query is not None:
      qs = qs.filter(Q(name__icontains=query)|Q(highlighted__icontains=query)).distinct()
    return qs

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

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