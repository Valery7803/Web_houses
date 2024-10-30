# Generated by Django 5.1.2 on 2024-10-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_house_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
