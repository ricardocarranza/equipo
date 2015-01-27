# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0017_auto_20150127_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=75, blank=True)),
                ('tipo', models.CharField(max_length=75, blank=True)),
                ('tamano', models.CharField(max_length=75, verbose_name=b'Tamao', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='monitor',
            field=models.ForeignKey(to='equipo.Monitor', null=True),
            preserve_default=True,
        ),
    ]
