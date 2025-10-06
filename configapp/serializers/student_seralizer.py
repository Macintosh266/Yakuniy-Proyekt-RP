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
        fields=['id','full_name','group','user','discription','is_line','address']
        read_only_fields=['id']

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


class StudentListSerializer(serializers.ListSerializer):
    """Bir nechta studentni update qilish uchun custom serializer"""
    def update(self, instances, validated_data):
        # instances -> querysetdagi studentlar
        # validated_data -> request.data'dan kelgan list
        student_mapping = {student.id: student for student in instances}
        data_mapping = {item['id']: item for item in validated_data}

        updated_students = []
        for student_id, data in data_mapping.items():
            student = student_mapping.get(student_id)
            if student:
                for attr, value in data.items():
                    setattr(student, attr, value)
                student.save()
                updated_students.append(student)

        return updated_students


class CheckSerializerStudent(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Students
        fields = ['id', 'is_line']  # faqat shu maydonni yangilaymiz
        read_only_fields = ['full_name', 'group', 'user', 'discription', 'address']
        list_serializer_class = StudentListSerializer
