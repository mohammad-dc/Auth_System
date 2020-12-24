from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
