# Generated by Django 4.0.3 on 2022-05-13 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sort', '0007_remove_sort_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]