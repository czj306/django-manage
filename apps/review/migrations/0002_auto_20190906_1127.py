# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-06 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('ctime',), 'verbose_name': '\u65e5\u5fd7', 'verbose_name_plural': '\u65e5\u5fd7'},
        ),
        migrations.AlterField(
            model_name='review',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='review',
            name='founder',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\xba'),
        ),
        migrations.AlterField(
            model_name='review',
            name='utime',
            field=models.DateTimeField(editable=False, null=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
