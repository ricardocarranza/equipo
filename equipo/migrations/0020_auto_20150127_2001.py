# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0019_auto_20150127_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichatecnica',
            name='periferico',
            field=models.ManyToManyField(to='equipo.Periferico'),
            preserve_default=True,
        ),
    ]
