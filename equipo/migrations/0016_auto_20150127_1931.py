# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0015_auto_20150127_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Red',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=75, blank=True)),
                ('modelo', models.CharField(max_length=75, blank=True)),
                ('tipo', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='red',
            field=models.ForeignKey(to='equipo.Red', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='moderboard',
            field=models.CharField(max_length=75, verbose_name=b'Motherboard'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='unidad',
            field=models.ManyToManyField(to='equipo.Unidad', verbose_name=b'Unidades Opticas'),
            preserve_default=True,
        ),
    ]
