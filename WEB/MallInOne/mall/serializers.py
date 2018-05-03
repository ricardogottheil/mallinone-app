from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Mall

class MallSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='mall:mall-highlight', format='html')

    class Meta:
        model = Mall
        fields = ('name', 'local', 'latitude', 'longitude', 'owner', 'highlight', 'image') 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    local = serializers.HyperlinkedRelatedField(
        many=True, view_name='UserViewSet', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'mall')