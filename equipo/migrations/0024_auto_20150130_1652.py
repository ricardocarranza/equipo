# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0023_auto_20150130_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75, blank=True)),
                ('version', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='otro',
            field=models.ManyToManyField(to='equipo.Otro', null=True, verbose_name=b'Navegador Web', blank=True),
            preserve_default=True,
        ),
    ]
