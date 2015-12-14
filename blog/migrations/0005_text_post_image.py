# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151022_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='text_post',
            name='image',
            field=models.TextField(default=b''),
        ),
    ]
