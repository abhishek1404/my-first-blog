# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_text_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='country',
            new_name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Published_Date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='language',
        ),
        migrations.RemoveField(
            model_name='post',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='Published_Date',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='country',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='language',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='text_post',
            name='tags',
        ),
    ]
