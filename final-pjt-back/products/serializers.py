from rest_framework import serializers
from .models import ProductList, ProductListOptions


class ProductListSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProductList
        fields = '__all__'
        read_only_fields = ('product_type',)


class ProductListOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProductListOptions
        fields = '__all__'
        read_only_fields = ('product',)