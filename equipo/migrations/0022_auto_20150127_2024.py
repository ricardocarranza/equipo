# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0021_auto_20150127_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antiv',
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
            name='antivirus',
            field=models.ForeignKey(verbose_name=b'Anti-virus', blank=True, to='equipo.Antiv', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='office',
            field=models.ForeignKey(verbose_name=b'Sistema ofimatico', blank=True, to='equipo.Ofimati', null=True),
            preserve_default=True,
        ),
    ]
