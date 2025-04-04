from rest_framework import serializers
from inventory.models import Category


class InventoryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'parent', 'name', 'slug', 'is_active', 'level']
        dump_only = ['id', 'name']