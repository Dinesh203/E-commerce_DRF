# Generated by Django 4.0.1 on 2022-01-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media/user_profile/default_image/default-user-photo-79.jpg', null=True, upload_to='user_profile'),
        ),
    ]
