# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0007_ram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ram',
            old_name='tipo',
            new_name='velocidad',
        ),
    ]
