# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Mall 
from .serializer import MallSerializer

from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Malls view")

class MallList(generics.ListCreateAPIView):
	queryset = Mall.objects.all()
	serializer_class = MallSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
		    )
		return obj