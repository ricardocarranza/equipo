# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0022_auto_20150127_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compresor',
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
            name='Grabador',
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
            name='Navegador',
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
            name='Pdf',
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
            name='compresor',
            field=models.ForeignKey(blank=True, to='equipo.Compresor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='grabador',
            field=models.ForeignKey(verbose_name=b'Grabador de archivos', blank=True, to='equipo.Grabador', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='navegador',
            field=models.ManyToManyField(to='equipo.Navegador', null=True, verbose_name=b'Navegador Web', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='visualpdf',
            field=models.ManyToManyField(to='equipo.Pdf', null=True, verbose_name=b'Visualizador pdf', blank=True),
            preserve_default=True,
        ),
    ]
