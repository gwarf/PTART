# Generated by Django 3.2.16 on 2024-05-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0032_retesthit'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='retesthit',
            constraint=models.UniqueConstraint(fields=('retest_campaign', 'hit'), name='unique hitretest'),
        ),
    ]
