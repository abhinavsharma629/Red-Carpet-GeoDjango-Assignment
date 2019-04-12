# Generated by Django 2.1.5 on 2019-04-12 05:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocation', '0011_auto_20190412_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='geojsonThroughFile',
            fields=[
                ('location_name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('data', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
    ]
