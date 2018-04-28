from .models import Product 

from django.contrib.auth.models import User
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='product:product-highlight', format='html')

	class Meta:
		model = Product
		fields = ('name', 'price', 'brand', 'characteristics', 'owner', 'highlight')
		
class UserSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        many=True, view_name='UserViewSet', read_only=True)#view_name='product:product-detail'
    #url = serializers.HyperlinkedIdentityField(view_name="product:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username', 'product')