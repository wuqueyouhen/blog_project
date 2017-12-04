# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'click_count')

    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'desc', 'content',)
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse',),
    #         'fields': ('click_count', 'is_recommend',)
    #     }),
    # )

    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
