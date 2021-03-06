# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import data.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('stop_ids', data.fields.ArrayField(unique=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('index', models.IntegerField()),
                ('stop_id', models.IntegerField(db_index=True)),
                ('stop_name', models.CharField(max_length=100)),
                ('is_skipped', models.BooleanField(default=False)),
                ('valid', models.BooleanField(default=False, db_index=True)),
                ('is_first', models.BooleanField(default=False)),
                ('is_last', models.BooleanField(default=False)),
                ('actual_arrival', models.DateTimeField(blank=True, null=True)),
                ('exp_arrival', models.DateTimeField(blank=True, null=True)),
                ('delay_arrival', models.FloatField(blank=True, null=True)),
                ('actual_departure', models.DateTimeField(blank=True, null=True)),
                ('exp_departure', models.DateTimeField(blank=True, null=True)),
                ('delay_departure', models.FloatField(blank=True, null=True)),
                ('data_file', models.CharField(max_length=100)),
                ('data_file_line', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('local_time_str', models.TextField(default=None)),
                ('route', models.ForeignKey(related_name='services', to='data.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.CharField(primary_key=True, unique=True, serialize=False, db_index=True, max_length=30)),
                ('valid', models.BooleanField(default=False)),
                ('trip_name', models.CharField(db_index=True, max_length=30)),
                ('train_num', models.IntegerField(db_index=True)),
                ('start_date', models.DateField(db_index=True)),
                ('route', models.ForeignKey(related_name='trips', to='data.Route')),
                ('service', models.ForeignKey(to='data.Service', related_name='trips', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='trip',
            field=models.ForeignKey(to='data.Trip', related_name='samples', null=True, blank=True),
        ),
    ]
