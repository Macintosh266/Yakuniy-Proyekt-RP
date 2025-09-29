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
        ref_name = "StudentAddUserSerializer"

class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=['full_name','group','user','discription','is_line','address']

class StudentSerializer(serializers.Serializer):
    users=AddUserSerializer()
    student=AddStudentSerializer()

class FAddStudentSerializer(serializers.ModelSerializer):
    user=AddUserSerializer()

    class Meta:
        model=Students
        fields=['full_name','group','user','discription','is_line','address']

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = AddUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save() 

        student = Students.objects.create(user=user, **validated_data)
        return student
    
class StudentChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("Parollar bir xil emas")
        return attrs