# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
User = get_user_model()


class Review(models.Model):

    title = models.CharField(max_length=20, verbose_name=u'日志标题')
    content = models.TextField(max_length=10000, verbose_name=u'日志内容')

    ctime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    utime = models.DateTimeField(null=True, verbose_name=u'修改时间', editable=False)
    creator = models.CharField(verbose_name=u'创建人', max_length=128, editable=False)

    class Meta:
        db_table = "reviews"
        verbose_name = u"日志"
        verbose_name_plural = u"日志"
        ordering = ('ctime',)

    def save(self, *args, **kwargs):
        created = self.id is None
        if created:
            try:
                self.ctime = datetime.now()
            except Exception:
                pass
        else:
            self.utime = datetime.now()

        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


