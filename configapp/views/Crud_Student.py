from django import views
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from yaml import serialize_all
from configapp.serializers.student_seralizer import *
from rest_framework.viewsets import ModelViewSet
from configapp.models.auth_user import User
from configapp.models.studentsmodel import *
from rest_framework.response import Response
from configapp.add_permission import *
from django.shortcuts import get_object_or_404
from configapp.serializers.email_seralizer import SendMassageSerializer
from django.core.mail import send_mail




class StudentRegister(APIView):
    permission_classes = [IsAdminPermission]

    @swagger_auto_schema(request_body=FAddStudentSerializer)
    def post(self, request):
        serializer = FAddStudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data.get("user")
        email = user_data.get("email")
        raw_password = user_data.get("password")   # oddiy parol

        # Avval student va userni yaratamiz
        student = serializer.save()

        # Endi foydalanuvchi parolini xashlab saqlash
        student.user.set_password(raw_password)
        student.user.save()

        # Email jo‘natish
        full_message = f"""
        Sizga Django tomonidan xabar yuborildi:
        email: {email}
        parol: {raw_password}
        """
        send_mail(
            subject="Tasdiqlash kodi",
            message=full_message,
            from_email="mtosh662@gmail.com",  # .com yozilishi kerak
            recipient_list=[email],
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentChangePassword(APIView):
    @swagger_auto_schema(request_body=StudentChangePasswordSerializer)
    def post(self, request):
        serializer = StudentChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data.get("old_password")):
            return Response(data={"message": "Eski parol noto'g'ri"}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data.get("new_password"))
        user.is_active=True
        user.save()
        return Response(data={"message": "Parol muvaffaqiyatli o'zgartirildi"}, status=status.HTTP_200_OK)
    


class StudentView(ModelViewSet):
    permission_classes=[IsStudentPermission]
    serializer_class = AddStudentSerializer
    queryset = Students.objects.all()



    # def get(self, request):
    #     student = Students.objects.all()
    #     serialiser = AddStudentSerializer(student, many=True)
    #     return Response(data=serialiser.data, status=status.HTTP_200_OK)
    #
    # @swagger_auto_schema(request_body=FAddStudentSerializer)
    # def patch(self, request, pk):
    #     student = get_object_or_404(Students, pk=pk)
    #     serializer = FAddStudentSerializer(student, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data={'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
    #
    # @swagger_auto_schema(request_body=AddStudentSerializer)
    # def put(self, request, pk):
    #     student = get_object_or_404(Students, pk=pk)
    #     serializer = AddStudentSerializer(student, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data={'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
    #
    # def delete(self, request, pk):
    #     student = get_object_or_404(Students, pk=pk)
    #     student.delete()
    #     return Response(data={'message': "Malumot o'chirildi"}, status=status.HTTP_204_NO_CONTENT)



