# Generated by Django 2.1.5 on 2019-04-11 17:14

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocation', '0003_geojson1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geojson1',
            name='data',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
        ),
    ]
