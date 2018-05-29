from rest_framework import serializers

from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [
      'pk',
      'local',
      'name',
      'price',
      'brand',
      'characteristics',
      'owner',
      'highlighted',
      'image',
    ]

    read_only_fields = ['pk']

    def validate_name(self, value):
      qs = Product.objects.filter(name__iexact=value)
      if self.instance:
        qs = qs.exclude(pk=self.instance.pk)
      if qs.exists():
        raise serializers.ValidationError("Este nombre ya esta en uso")
      return value


  # converts to JSON
  # validations for data passed