# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mensajes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='mensaje',
            new_name='contenido',
        ),
    ]
