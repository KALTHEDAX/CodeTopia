# Generated by Django 3.0.2 on 2020-01-31 10:47

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200129_1313'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default=account.models.get_default_profile_pic_path, upload_to=account.models.get_profile_pic_path, verbose_name='Profile Picture'),
        ),
    ]
