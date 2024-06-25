# Generated by Django 4.2.13 on 2024-06-25 01:50

from django.db import migrations, models

def init_screenshot_order(apps, schema_editor):
    Hit = apps.get_model('ptart', 'Hit')
    for hit in Hit.objects.all():
        screenshot_order = 0
        for screenshot in hit.screenshot_set.all().order_by('id'):
            screenshot.order = screenshot_order
            screenshot_order += 1
            screenshot.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0034_alter_project_pentesters_alter_project_viewers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screenshot',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='screenshot',
            name='order',
            field=models.IntegerField(default=-1),
        ),
        migrations.RunPython(init_screenshot_order),
    ]
