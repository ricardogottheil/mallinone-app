from django.contrib.auth.models import User
from rest_framework import serializers

from local.models import Local


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='local-highlight', format='html')

    class Meta:
        model = Local
        fields = ('id', 'name', 'owner', 'highlight') #'product'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    local = serializers.HyperlinkedRelatedField(
        many=True, view_name='local-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'local')
