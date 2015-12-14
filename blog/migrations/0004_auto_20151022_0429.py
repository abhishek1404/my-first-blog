# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151022_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type_p',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='text_post',
            name='type_p',
            field=models.TextField(default=b''),
        ),
    ]
