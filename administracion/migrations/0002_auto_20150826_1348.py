# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='suplidor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Suplidores'},
        ),
        migrations.AlterModelOptions(
            name='tiposuplidor',
            options={'ordering': ['descripcion'], 'verbose_name': 'Tipo de Suplidor', 'verbose_name_plural': 'Tipos de Suplidores'},
        ),
    ]
