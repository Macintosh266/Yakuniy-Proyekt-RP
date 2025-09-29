from rest_framework import serializers
from configapp.models.teachersmodel import *


class AddUserSerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    is_teacher=serializers.BooleanField(read_only=True)
    is_student=serializers.BooleanField(read_only=True)
    is_admin=serializers.BooleanField(read_only=True)

    class Meta:
        model=User
        fields=['phone','email','password','is_active','is_teacher','is_student','is_admin']
        ref_name='TeacherAddUserSerializer'

class AddTeacherSerializer(serializers.ModelSerializer):
    # user=AddUserSerializer()
    class Meta:
        model=Teacher
        fields = ['full_name','discription']
        read_only_fields=['user']

class STeacherSerializer(serializers.Serializer):
    user=AddUserSerializer()
    teacher=AddTeacherSerializer()



class FTeacherSerializer(serializers.ModelSerializer):
    user=AddUserSerializer()

    class Meta:
        model=Teacher
        fields = ['full_name', 'discription','user','departament','course']


    def create(self, validated_data):
        user_db=validated_data.pop('user')
        departments_db=validated_data.pop('department')
        course_db=validated_data.pop('course')
        user_db['is_active']=True
        user_db['is_teacher']=True
        user=User.objects.create_user(**user_db)
        teacher=Teacher.objects.create(user=user,**validated_data)
        teacher.departments.set(departments_db)
        teacher.course.set(course_db)
        return teacher