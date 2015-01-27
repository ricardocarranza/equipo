# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='puesto',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(max_length=9, blank=True),
            preserve_default=True,
        ),
    ]
