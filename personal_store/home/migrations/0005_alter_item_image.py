# Generated by Django 5.0 on 2024-05-24 21:11

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_item_buycount_item_category_item_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=home.models.getImagePath),
        ),
    ]
