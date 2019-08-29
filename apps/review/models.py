# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Review(models.Model):

    title = models.CharField(max_length=20, verbose_name=u'名称')

    class Meta:
        db_table = "reviews"
        verbose_name_plural = u"日志"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class FileSimpleModel(models.Model):
    """
    文件接收 Model
    upload_to：表示文件保存位置
    """
    file_field = models.FileField(upload_to="upload/%Y/%m/%d")
