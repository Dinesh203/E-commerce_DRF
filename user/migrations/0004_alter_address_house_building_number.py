# Generated by Django 4.0.1 on 2022-01-11 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='house_building_number',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
