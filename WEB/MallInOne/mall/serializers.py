from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Mall

class MallSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Mall
        fields = ('name', 'owner', 'highlighted', 'image', 'map_url') 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    local = serializers.HyperlinkedRelatedField(
        many=True, view_name='UserViewSet', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'mall')