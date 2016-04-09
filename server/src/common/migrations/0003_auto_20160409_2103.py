# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20160409_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesmappedto',
            name='services',
        ),
        migrations.DeleteModel(
            name='ServicesMappedTo',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
