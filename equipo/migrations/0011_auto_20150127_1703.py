# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0010_auto_20150127_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidad',
            name='marca',
            field=models.CharField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unidad',
            name='velocidad',
            field=models.CharField(max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
