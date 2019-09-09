# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'ctime', 'utime']
    list_filter = ['ctime']

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.creator = request.user.username
        obj.save()


admin.site.register(Review, ReviewAdmin)
admin.site.site_title = "站点控制中心"
admin.site.site_header = "站点控制中心"
admin.site.index_title = "站点控制中心"
