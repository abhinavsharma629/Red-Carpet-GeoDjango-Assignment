# Generated by Django 2.1.5 on 2019-04-11 18:35

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocation', '0008_auto_20190412_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geojson',
            name='data',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='geojson',
            name='data1',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
    ]
