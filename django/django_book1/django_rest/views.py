from rest_framework import viewsets

from django.shortcuts import render
from django.views import generic

from programmers_test.models import (
    Gender, Category, Item, Ingredient
)
from programmers_test.views import resonpse_in_json
from .serializers import ItemSerializer


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemView(generic.View):
    @resonpse_in_json
    def get(self, request):
        print('=================')
        items = Item.objects.all()
        # items = [item.get_json(0) for item in items]
        print('=================', items)
        serializer = ItemSerializer(items, many=True, context={'request': request})
        print('=================', serializer)
        try:
            print('=================', serializer.data)
        except Exception as err:
            print('================= err ', err)
        return serializer.data
        # return items
        