# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AfgScrEventtypecat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cat_name', models.CharField(max_length=255, blank=True)),
                ('name_short', models.CharField(max_length=255, blank=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'afg_scr_eventtypecat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AfgScrIncidenttargetcat',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('cat_name', models.CharField(max_length=255)),
                ('name_short', models.CharField(max_length=255, blank=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'afg_scr_incidenttargetcat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('evnt_name', models.CharField(max_length=255)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
                ('evnt_cat', models.ForeignKey(db_column=b'evnt_cat', blank=True, to='securitydb.AfgScrEventtypecat', null=True)),
            ],
            options={
                'db_table': 'afg_scr_eventtype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='IncidentTarget',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('inct_name', models.CharField(max_length=255)),
                ('inct_short', models.CharField(max_length=255, null=True, blank=True)),
                ('inct_description', models.CharField(max_length=400, null=True, blank=True)),
                ('inct_scoring', models.IntegerField(null=True, blank=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
                ('inct_catid', models.ForeignKey(db_column=b'inct_catid', blank=True, to='securitydb.AfgScrIncidenttargetcat', null=True)),
            ],
            options={
                'db_table': 'afg_scr_incidenttarget',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SecureFeature',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('scre_notes', models.TextField(null=True, blank=True)),
                ('scre_username', models.CharField(max_length=255, blank=True)),
                ('scre_sourcename', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_incidentdatestr', models.CharField(max_length=10)),
                ('scre_incidenttimestr', models.CharField(max_length=5)),
                ('scre_incidentdate', models.DateTimeField(null=True, blank=True)),
                ('scre_eventname', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_incidenttargetname', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_violent', models.BooleanField(default=False)),
                ('scre_unknown', models.BooleanField(default=False)),
                ('scre_arrested', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('scre_injured', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('scre_dead', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('scre_provid', models.IntegerField(null=True, blank=True)),
                ('scre_provname', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_distid', models.IntegerField(null=True, blank=True)),
                ('scre_distname', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_placename', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_latitude', models.FloatField(null=True, blank=True)),
                ('scre_longitude', models.FloatField(null=True, blank=True)),
                ('mpoint', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
                ('scre_settvuid', models.CharField(max_length=255, null=True, blank=True)),
                ('scre_eventid', models.ForeignKey(to='securitydb.EventType')),
                ('scre_incidenttarget', models.ForeignKey(to='securitydb.IncidentTarget')),
            ],
            options={
                'db_table': 'afg_scr_securefeature',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SourceGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('scrg_name', models.CharField(max_length=255, blank=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'afg_scr_sourcegroup',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('scrc_name', models.CharField(max_length=255, blank=True)),
                ('scrc_description', models.CharField(max_length=400, null=True, blank=True)),
                ('scrc_url', models.CharField(max_length=255, null=True, blank=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('entrydatetime', models.DateTimeField(null=True, blank=True)),
                ('userud', models.IntegerField(null=True, blank=True)),
                ('updatedatetime', models.DateTimeField(null=True, blank=True)),
                ('recstatus', models.IntegerField(null=True, blank=True)),
                ('scrc_scrgid', models.ForeignKey(db_column=b'scrc_scrgid', blank=True, to='securitydb.SourceGroup', null=True)),
            ],
            options={
                'db_table': 'afg_scr_sourcetype',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='securefeature',
            name='scre_sourceid',
            field=models.ForeignKey(to='securitydb.SourceType'),
        ),
    ]
