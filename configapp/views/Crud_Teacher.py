from django import views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from configapp.serializers.teacher_seralizer import *
from rest_framework.viewsets import ModelViewSet
from configapp.models.auth_user import *
from configapp.serializers.email_seralizer import *


class TeacherView(APIView):
    # @swagger_auto_schema(request_body=FTeacherSerializer)
    # def post(self,request):
    #     serializer=FTeacherSerializer(data=request.data)
    #     serializer.is_valid()
    #
    #
    #     try:
    #         tp=TimePassword.objects.filter(email=email)
    #     except TimePassword.DoesNotExist:
    #         return Response({"error": "Bu email uchun OTP yuborilmagan"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     if not tp.is_bool:
    #         return Response({"error": "Email OTP orqali tasdiqlanmagan"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     serializer.save()
    #     tp.delete()
    #     return Response(data=serializer.data,status=status.HTTP_201_CREATED)

    def get(self, request):
        teacher=Teacher.objects.all()
        serialiser=FTeacherSerializer(teacher,many=True)
        return Response(data=serialiser.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=FTeacherSerializer)
    def patch(self, request,pk):
        teacher=get_object_or_404(Teacher,pk=pk)
        serializer = FTeacherSerializer(teacher,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'success':True,'data':serializer.data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=FTeacherSerializer)
    def put(self, request,pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = FTeacherSerializer(teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def delete(self, request,pk):
        teacher=get_object_or_404(Teacher,pk=pk)
        teacher.delete()
        return Response(data={'message':"Malumot o'chirildi"},status=status.HTTP_204_NO_CONTENT)

#
# class TeacherView(ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = TeacherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user_id = request.data.get('user')
#         user = User.objects.filter(pk=user_id).first()
#
#         if not user:
#             return Response({"message": "Bunday user topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
#
#         if not user.is_teacher:
#             return Response({"message": "Bu user teacher emas!"}, status=status.HTTP_400_BAD_REQUEST)
#
#         if Teacher.objects.filter(user=user).exists():
#             return Response({"message": "Bunday o'qituvchi allaqachon mavjud!"}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

