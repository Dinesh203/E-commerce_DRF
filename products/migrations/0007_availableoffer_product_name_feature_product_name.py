# Generated by Django 4.0.1 on 2022-01-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_feature_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableoffer',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
