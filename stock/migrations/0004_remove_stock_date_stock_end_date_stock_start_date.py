# Generated by Django 4.2.1 on 2023-06-08 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_stock_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='date',
        ),
        migrations.AddField(
            model_name='stock',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]