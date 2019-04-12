# Generated by Django 2.1.5 on 2019-04-11 18:32

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.polygon
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocation', '0006_auto_20190411_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='geojson',
            name='data1',
            field=django.contrib.gis.db.models.fields.GeometryField(default=django.contrib.gis.geos.polygon.Polygon(((1, 1), (1, 2), (2, 2), (1, 1))), srid=4326),
        ),
    ]
