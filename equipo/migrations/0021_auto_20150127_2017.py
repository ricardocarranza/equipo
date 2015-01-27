# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0020_auto_20150127_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ofimati',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75, blank=True)),
                ('version', models.CharField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sistema',
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
            name='office',
            field=models.ForeignKey(verbose_name=b'Sistema operativo', blank=True, to='equipo.Ofimati', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='sistema',
            field=models.ForeignKey(verbose_name=b'Sistema operativo', blank=True, to='equipo.Sistema', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='usuario',
            field=models.ForeignKey(blank=True, to='equipo.Usuario', null=True),
            preserve_default=True,
        ),
    ]
