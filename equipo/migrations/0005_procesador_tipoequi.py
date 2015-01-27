# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(help_text=b'Ingrese el nombre del modelo de microprocesador', max_length=75)),
                ('modelo', models.CharField(max_length=75)),
                ('velocidad', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEqui',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=75, verbose_name=b'Tipo de equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
