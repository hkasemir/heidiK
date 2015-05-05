# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincontent',
            name='page',
            field=models.CharField(default='index', max_length=20),
        ),
    ]
