from rest_framework import serializers
from ..models import *

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Homework
        fields='__all__'
        read_only_fields=['group']


class CheckHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomeworkGet
        fields=['ball','homework','student','is_submitted']
        read_only_fields=['is_submitted']

class DoHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomeworkGet
        fields=['submission_file','homework','student']
