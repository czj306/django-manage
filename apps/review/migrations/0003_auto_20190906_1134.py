# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-06 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20190906_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='founder',
            new_name='creator',
        ),
    ]
