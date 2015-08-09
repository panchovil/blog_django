# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Todas las Entradas',
            },
        ),
    ]
