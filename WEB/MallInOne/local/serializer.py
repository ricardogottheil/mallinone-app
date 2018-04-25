from .models import Local

from rest_framework import serializers

class LocalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Local
		fields = ('id', 'name', 'product')