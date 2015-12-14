# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text_Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.TextField(default=b'auth.User')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
                ('tags', models.TextField(default=b'')),
                ('country', models.TextField(default=b'')),
                ('language', models.TextField(default=b'')),
                ('content', models.TextField(default=b'')),
                ('release_date', models.TextField(default=b'')),
                ('Published_Date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='Created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='release_date',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(default=b'auth.User'),
        ),
    ]
