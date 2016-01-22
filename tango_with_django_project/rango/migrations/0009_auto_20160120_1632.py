# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20160115_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapas',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
