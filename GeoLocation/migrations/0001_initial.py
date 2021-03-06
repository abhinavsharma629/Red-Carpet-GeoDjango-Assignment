# Generated by Django 2.1.5 on 2019-04-11 16:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comparisonDataBySelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centerlatitude', models.FloatField(default=0.0)),
                ('centerlongitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('location_key', models.CharField(max_length=200)),
                ('radius', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='comparisonDataForPostgres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centerlatitude', models.FloatField(default=0.0)),
                ('centerlongitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('location_key', models.CharField(max_length=200)),
                ('radius', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='geojson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=1000)),
                ('data', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='placeAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=1000)),
                ('location_check', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='spatialData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('place_name', models.CharField(max_length=200)),
                ('city_name', models.CharField(max_length=200)),
                ('latitude', models.FloatField(blank=True, default=0.0, null=True)),
                ('longitude', models.FloatField(blank=True, default=0.0, null=True)),
                ('latitude_longitude', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('accuracy', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
