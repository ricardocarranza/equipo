# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0014_fichatecnica_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=75, blank=True)),
                ('puerto', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=75, blank=True)),
                ('puerto', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='mouse',
            field=models.ForeignKey(to='equipo.Mouse', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='teclado',
            field=models.ForeignKey(to='equipo.Teclado', null=True),
            preserve_default=True,
        ),
    ]
