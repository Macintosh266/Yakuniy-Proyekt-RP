from rest_framework import serializers
from configapp.models.teachersmodel import *


class AddUserSerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    is_teacher=serializers.BooleanField(read_only=True)
    is_student=serializers.BooleanField(read_only=True)
    is_admin=serializers.BooleanField(read_only=True)

    class Meta:
        model=User
        fields=['username','phone','email','password','is_active','is_teacher','is_student','is_admin']
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


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departmenrt
        fields='__all__'


class FTeacherSerializer(serializers.ModelSerializer):
    course=CourseSerializer()
    departament=DepartamentSerializer()
    user=AddUserSerializer()

    class Meta:
        model=Teacher
        fields = ['full_name', 'discription','user','departament','course']


    def create(self, validated_data):
        user_db=validated_data.pop('user')
        departments_db=validated_data.pop('departament')
        course_db=validated_data.pop('course')
        user_db['is_active']=True
        user_db['is_teacher']=True
        user=User.objects.create_user(**user_db)
        teacher=Teacher.objects.create(user=user,**validated_data)
        courses=[]
        for cour in course_db:
            course, _ = Course.objects.get_or_create(**cour)
            courses.append(course)
        teacher.course.set(courses)
        departments = []
        for dep in departments_db:
            department, _ = Departmenrt.objects.get_or_create(**dep)
            departments.append(department)
        teacher.department.set(departments)
        return teacher