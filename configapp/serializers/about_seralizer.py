from rest_framework import serializers
from ..models import *


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        fields='__all__'


class ServesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Serves
        fields='__all__'
        