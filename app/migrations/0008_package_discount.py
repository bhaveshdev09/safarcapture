# Generated by Django 5.0 on 2024-01-25 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_package_card_cover_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)]),
        ),
    ]
