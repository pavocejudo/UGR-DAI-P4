# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20160113_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapas',
            name='picture',
            field=models.ImageField(upload_to=b'bares/', blank=True),
        ),
    ]
