from .models import Mall

from rest_framework import serializers

class MallSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mall
		fields = ('name', 'local')