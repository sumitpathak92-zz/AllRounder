# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='join_date',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
    ]
