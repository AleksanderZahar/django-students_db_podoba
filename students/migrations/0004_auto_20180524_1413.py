# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20180524_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title'], 'verbose_name': '\u0413\u0440\u0443\u043f\u0430', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438'},
        ),
    ]
