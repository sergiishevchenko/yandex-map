# Generated by Django 3.2.16 on 2022-11-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='coordinate_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='coordinate_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, null=True),
        ),
    ]
