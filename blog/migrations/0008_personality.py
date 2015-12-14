# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151105_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
                ('image', models.TextField(default=b'')),
                ('metadata', models.TextField(default=b'')),
            ],
        ),
    ]
