# Generated by Django 2.2.24 on 2022-04-21 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0011_label_deprecated'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=''),
        ),
    ]
