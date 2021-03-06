# Generated by Django 4.0.3 on 2022-05-12 17:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sort', '0004_sortitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(1)])),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('delete_flg', models.BooleanField()),
                ('login_time', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sort',
            name='user_id',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999999)])),
                ('delete_flg', models.BooleanField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('sort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='sort.sort')),
            ],
        ),
        migrations.AddField(
            model_name='sort',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='sorts', to='sort.user'),
            preserve_default=False,
        ),
    ]
