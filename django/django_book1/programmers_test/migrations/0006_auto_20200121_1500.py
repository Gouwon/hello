# Generated by Django 2.2.4 on 2020-01-21 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmers_test', '0005_auto_20200120_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_text',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]