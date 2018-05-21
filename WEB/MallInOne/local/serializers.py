from django.contrib.auth.models import User
from rest_framework import serializers

from local.models import Local

class LocalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Local
        fields = ('name', 'mall', 'owner', 'image', 'map_url', 'highlighted')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    local = serializers.HyperlinkedRelatedField(
        many=True, view_name='UserViewSet', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'local')