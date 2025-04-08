from rest_framework import serializers
from inventory.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'parent', 'name', 'slug', 'is_active', 'level']
        dump_only = ['id', 'name']



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category']


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "is_digital",
            "is_active",
            "price",
            "category",
        ]