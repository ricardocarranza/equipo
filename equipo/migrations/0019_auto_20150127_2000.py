# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0018_auto_20150127_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periferico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75, blank=True)),
                ('marca', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='periferico',
            field=models.ManyToManyField(to='equipo.Periferico', verbose_name=b'Unidades Opticas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monitor',
            name='tamano',
            field=models.CharField(max_length=75, verbose_name=b'Tamanio', blank=True),
            preserve_default=True,
        ),
    ]
