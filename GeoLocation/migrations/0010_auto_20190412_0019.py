# Generated by Django 2.1.5 on 2019-04-11 18:49

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.polygon
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocation', '0009_auto_20190412_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geojson',
            name='data1',
        ),
        migrations.AlterField(
            model_name='geojson',
            name='data',
            field=django.contrib.gis.db.models.fields.GeometryField(default=django.contrib.gis.geos.polygon.Polygon(((3, 3), (3, 3), (3, 3), (3, 3))), srid=4326),
        ),
    ]
