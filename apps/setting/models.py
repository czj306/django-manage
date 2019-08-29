# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Setting(models.Model):

    title = models.CharField(max_length=20, verbose_name=u'名称')

    class Meta:
        db_table = "setting"
        verbose_name_plural = u"设置"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

