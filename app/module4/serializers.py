from rest_framework import serializers
from inventory.models import Category, Product, StockManagement


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


class StockManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockManagement
        fields = ["quantity"]


class ProductStockSerializer(serializers.ModelSerializer):
    stock = StockManagementSerializer(read_only=True)

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
            "stock"
        ]


class CreateProductStockSerializer(serializers.ModelSerializer):
    stock = StockManagementSerializer(write_only=True, required=True)

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
            "stock"
        ]

    def create(self, validated_data):
        product_stock_data = validated_data.pop('stock', None)
        product = Product.objects.create(**validated_data)
        if product_stock_data:
            product.stock = StockManagement.objects.create(product=product, **product_stock_data)
        return product

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # stock_instance = StockManagement.objects.filter(product=instance).first()
        stock_instance = instance.stock

        if stock_instance:
            data["stock"] = StockManagementSerializer(stock_instance).data
        else:
            data["stock"] = None  
        return data
