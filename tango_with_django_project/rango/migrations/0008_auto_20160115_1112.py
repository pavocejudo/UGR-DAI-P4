# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_tapas_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapas',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
