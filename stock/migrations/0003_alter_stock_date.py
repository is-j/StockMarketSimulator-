# Generated by Django 4.2.1 on 2023-06-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_remove_stock_current_price_remove_stock_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateField(),
        ),
    ]
