# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesMappedTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=100)),
                ('join_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='servicesmappedto',
            name='services',
            field=models.ForeignKey(to='common.Users'),
        ),
    ]
