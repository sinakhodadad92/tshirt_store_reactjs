from typing_extensions import Required
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_field=False, allow_null=True, required=False)
    class Meta: 
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')