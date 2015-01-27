# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0008_auto_20150127_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=75)),
                ('capacidad', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='disco',
            field=models.ForeignKey(verbose_name=b'Disco Duro', blank=True, to='equipo.Disco', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='procesador',
            field=models.ForeignKey(to='equipo.Procesador', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ram',
            name='capacidad',
            field=models.CharField(help_text=b'Ingrese la capacidad de la memoria (128MB - 4GB)', max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
