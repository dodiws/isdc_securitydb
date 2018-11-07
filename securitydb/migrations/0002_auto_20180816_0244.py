# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securitydb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='afgscreventtypecat',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='afgscrincidenttargetcat',
            options={'managed': True},
        ),
    ]
