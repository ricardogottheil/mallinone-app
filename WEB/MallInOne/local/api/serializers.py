from rest_framework import serializers

from local.models import Local

class LocalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Local
    fields = [
      'pk',
      'name',
      'mall',
      'owner',
      'highlighted',
      'image',
      'map_url',
    ]

    read_only_fields = ['pk']

    def validate_name(self, value):
      qs = Local.objects.filter(name__iexact=value)
      if self.instance:
        qs = qs.exclude(pk=self.instance.pk)
      if qs.exists():
        raise serializers.ValidationError("Este nombre ya esta en uso")
      return value

  # converts to JSON
  # validations for data passed