# Generated by Django 2.1.7 on 2019-03-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='timecode',
            field=models.FloatField(blank=True, null=True, verbose_name='timecode'),
        ),
    ]