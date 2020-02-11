from rest_framework import serializers

from .models import (Gender, Category, Ingredient, Item)

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='programmers_test:item_detail', format='html'
    )
    class Meta:
        model = Item
        fields = [
            'url', 'id', 'name', 'category', 'gender', 'price', 
            'monthly_sales', 'ingredients', 'image_id',
        ]