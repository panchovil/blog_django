# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150806_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['-fecha'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Todas las Entradas'},
        ),
    ]
