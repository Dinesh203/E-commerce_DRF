# Generated by Django 4.0.1 on 2022-01-20 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_collections_delete_collectionofcategories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='categories_name',
        ),
        migrations.AddField(
            model_name='category',
            name='collections',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.collections'),
        ),
        migrations.AddField(
            model_name='collections',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='collection/'),
        ),
    ]
