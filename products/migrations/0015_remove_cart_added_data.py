# Generated by Django 4.0.1 on 2022-01-22 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='added_data',
        ),
    ]
