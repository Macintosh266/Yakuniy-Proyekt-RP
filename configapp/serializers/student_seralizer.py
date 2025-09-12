from rest_framework import serializers
from configapp.models.studentsmodel import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=['name','surname','address','user']
        # read_only_fields=['user']