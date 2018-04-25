# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer

class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
		    )
		return obj