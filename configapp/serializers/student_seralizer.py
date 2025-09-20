from rest_framework import serializers
from configapp.models.studentsmodel import *

class AddUserSerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    is_teacher=serializers.BooleanField(read_only=True)
    is_student=serializers.BooleanField(read_only=True)
    is_admin=serializers.BooleanField(read_only=True)

    class Meta:
        model=User
        fields=['phone','email','password','is_active','is_teacher','is_student','is_admin']

class AddStudentSerializer(serializers.ModelSerializer):
    user=AddUserSerializer(

    )
    class Meta:
        model=Students
        fields=['full_name','group','user','discription','is_line','address']
        # read_only_fields=['user']


class StudentSerializer(serializers.Serializer):
    users=AddUserSerializer()
    student=AddStudentSerializer()

class FAddStudentSerializer(serializers.ModelSerializer):
    user=AddUserSerializer()

    class Meta:
        model=Students
        fields=['full_name','group','user','discription','is_line','address']

    def create(self,validated_data):
        pass