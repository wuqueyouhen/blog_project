# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 引用日志模块
import logging

from django.shortcuts import render
from django.conf import settings


logger = logging.getLogger('blog.views')


# Create your views here.
# 创建通用方法，调用settings.py中的定义的字段。注册本方法到settings.py中context_processors
# 需要一个参数，如果不加会报错
def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }


def index(request):
    try:
        # 打开文件，并不存在，触发异常
        file = open('aaa.txt', 'r')
    except Exception as e:
        # 讲异常写入log/error.log
        logger.error(e)
    return render(request, 'index.html', locals())
