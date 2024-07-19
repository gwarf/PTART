# Generated by Django 3.2.16 on 2024-05-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0031_retestcampaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetestHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Network'), ('NF', 'Adjacent'), ('PF', 'Local'), ('NA', 'Physical'), ('NT', 'Local')], max_length=2)),
                ('body', models.TextField(blank=True, default='')),
                ('hit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ptart.hit')),
                ('retest_campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ptart.retestcampaign')),
            ],
            options={
                'ordering': ('hit',),
            },
        ),
    ]
