# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0005_procesador_tipoequi'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichaTecnica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75, verbose_name=b'PC')),
                ('moderboard', models.CharField(max_length=75, verbose_name=b'Moder Board')),
                ('estado', models.ForeignKey(to='equipo.Estado')),
                ('procesador', models.ForeignKey(to='equipo.Procesador')),
                ('tipo', models.ForeignKey(to='equipo.TipoEqui')),
                ('usuario', models.ForeignKey(to='equipo.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='procesador',
            name='modelo',
            field=models.CharField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='procesador',
            name='velocidad',
            field=models.CharField(max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
