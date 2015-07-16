# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150716_1022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
