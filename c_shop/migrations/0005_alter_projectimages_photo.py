# Generated by Django 3.2.22 on 2023-10-30 02:13

import c_shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_shop', '0004_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=c_shop.models.rename_imagefile_to_uuid),
        ),
    ]
