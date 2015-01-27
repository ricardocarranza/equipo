# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0006_auto_20150126_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=75, blank=True)),
                ('tipo', models.CharField(max_length=75, blank=True)),
                ('buz', models.CharField(max_length=75, blank=True)),
                ('capacidad', models.CharField(help_text=b'Ingrese la capaciadad de la memoria (128MB - 4GB)', max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
