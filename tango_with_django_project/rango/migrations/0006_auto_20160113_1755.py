# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20160112_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapas',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 1, 13, 17, 55, 20, 449938, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bar',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
    ]
