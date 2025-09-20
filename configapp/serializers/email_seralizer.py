from rest_framework import serializers
from configapp.models.auth_user import *


class SendMassageSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ChackMassageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=6)

