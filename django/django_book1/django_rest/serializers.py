from rest_framework import serializers

from programmers_test.models import (
    Gender, Category, Item, Ingredient
)

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'image_id',
            'name',
            'price',
            'monthly_sales',
            'gender',
            'category',
            'ingredients',
        )