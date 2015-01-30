# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0024_auto_20150130_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichatecnica',
            name='observa',
            field=models.TextField(null=True, verbose_name=b'Observaciones', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='otro',
            field=models.ManyToManyField(to='equipo.Otro', null=True, verbose_name=b'Otros', blank=True),
            preserve_default=True,
        ),
    ]
