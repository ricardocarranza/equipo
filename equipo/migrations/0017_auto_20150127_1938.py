# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0016_auto_20150127_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
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
            name='impresora',
            field=models.ForeignKey(to='equipo.Print', null=True),
            preserve_default=True,
        ),
    ]
