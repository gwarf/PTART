# Generated by Django 2.2.8 on 2020-09-08 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0007_hit_displayable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='scope',
            new_name='introduction',
        ),
    ]