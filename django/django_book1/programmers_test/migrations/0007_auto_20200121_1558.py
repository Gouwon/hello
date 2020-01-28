# Generated by Django 2.2.4 on 2020-01-21 06:58

import os
import json
from django.db import migrations


FILE_NAME = 'data/items-data.json'
FILE_LOCATION = os.path.join(\
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), \
    FILE_NAME)

def get_json_data(FILE_LOCATION):
    with open(FILE_LOCATION) as f:
        data = json.load(f)
        result = []
        for datum in data:
            result.append(datum)
            if len(result) == 100:
                yield result
                result = []
        yield result

def insert_ingredients(ingredients_list, Item):
    ThroughModel = Item.ingredients.through

    for ingredients in ingredients_list:
        item_id = ingredients['id']
        ingredients['ingredients'] = [
            ThroughModel(item_id=item_id, ingredient_id=ingredient_id) 
                for ingredient_id in ingredients['ingredients']
        ]
        ThroughModel.objects.bulk_create(ingredients['ingredients'], \
            ignore_conflicts=True)

def insert_item(apps, schema_editor):
    Item = apps.get_model('programmers_test', 'Item')
    Gender = apps.get_model('programmers_test', 'Gender')
    Category = apps.get_model('programmers_test', 'Category')
    Ingredient = apps.get_model('programmers_test', 'Ingredient')

    json_data = get_json_data(FILE_LOCATION)

    gender_dictionary = {'all': 0, 'male': 1, 'female': 2}

    for data in json_data:
        item_list = []
        ingredients_list = []
        for datum in data:
            datum['image_id'] = datum.pop('imageId', '')
            datum['monthly_sales'] = datum.pop('monthlySales', '')
            gender = {'gender': gender_dictionary[datum['gender']]}
            datum['gender'] = Gender.objects.get_or_create(**gender)[0]
            category = {'category': datum['category']}
            datum['category'] = Category.objects.get_or_create(**category)[0]
            ingredients = datum.pop('ingredients', '').split(',')
            ingredients = [
                Ingredient.objects.get_or_create(name=name)[0].id 
                    for name in ingredients
            ]
            ingredients_data = {'id':datum['id'], 'ingredients': ingredients}
            ingredients_list.append(ingredients_data)
            it = Item(**datum)
            print('\n\n it >>>>> ', it, datum['name'])
            item_list.append(it)
        print('\n\n\n item_list >>>>> ', item_list)
        Item.objects.bulk_create(item_list)
        insert_ingredients(ingredients_list, Item)


class Migration(migrations.Migration):

    dependencies = [
        ('programmers_test', '0006_auto_20200121_1500'),
    ]

    operations = [
        migrations.RunPython(insert_item),
    ]
