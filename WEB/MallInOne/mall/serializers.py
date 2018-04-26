from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Mall

class MallSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='mall-highlight', format='html')

    class Meta:
        model = Mall
        fields = ('name', 'owner', 'highlight') #'local'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    local = serializers.HyperlinkedRelatedField(
        many=True, view_name='mall-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'mall')