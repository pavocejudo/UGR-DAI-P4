# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160104_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
