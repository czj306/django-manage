from rest_framework import serializers
from django.contrib.auth.models import User
from menus.models import *
from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"


class LatestReleaseSerializer(serializers.ModelSerializer):
    # 最新发布
    founder = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Essay
        fields = ('id', 'title')


class MenusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menus
        fields = "__all__"


class EssaySerializer(serializers.ModelSerializer):
    parent = MenusSerializer(many=True)
    founder = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Essay
        fields = "__all__"

        