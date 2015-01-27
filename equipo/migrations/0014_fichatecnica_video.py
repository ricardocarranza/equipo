# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0013_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichatecnica',
            name='video',
            field=models.ForeignKey(to='equipo.Video', null=True),
            preserve_default=True,
        ),
    ]
