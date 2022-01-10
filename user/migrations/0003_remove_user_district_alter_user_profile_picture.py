# Generated by Django 4.0.1 on 2022-01-10 20:37

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_city_user_village_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='district',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=user.models.user_profile),
        ),
    ]
