# Generated by Django 2.1.5 on 2019-04-11 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocation', '0005_auto_20190411_2256'),
    ]

    operations = [
        migrations.DeleteModel(
            name='geojson1',
        ),
        migrations.DeleteModel(
            name='placeAddress',
        ),
    ]
