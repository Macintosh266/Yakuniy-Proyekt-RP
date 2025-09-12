from rest_framework import serializers
from configapp.models.teachersmodel import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields = ['name', 'surname', 'address','user']
        # read_only_fields = []