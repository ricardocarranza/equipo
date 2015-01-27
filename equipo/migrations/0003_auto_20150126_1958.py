# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20150126_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(max_length=9, null=True, blank=True),
            preserve_default=True,
        ),
    ]
