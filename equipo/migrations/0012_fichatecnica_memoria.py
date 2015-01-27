# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0011_auto_20150127_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichatecnica',
            name='memoria',
            field=models.ForeignKey(to='equipo.Ram', null=True),
            preserve_default=True,
        ),
    ]
