# -*- coding: utf-8 -*-
from .models import *
from .serializers import *
from rest_framework import mixins, viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    """
    list:
        日志表数据
    retrieve:
        获取日志详情
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

