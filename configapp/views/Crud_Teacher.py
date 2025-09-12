from django import views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from configapp.serializers.teacher_seralizer import *
from rest_framework.viewsets import ModelViewSet


# class TeacherView(APIView):
#     @swagger_auto_schema(request_body=TeacherSerializer)
#     def post(self,request):
#         user=User.objects.filter(is_teacher=True)
#
#         if user.exists():
#             return Response(data={"message":"Bunday o'qituvchi mavjud!"},status=status.HTTP_400_BAD_REQUEST )
#
#         serializer=TeacherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#
#     def get(self, request):
#         teacher=Teacher.objects.all()
#         serialiser=TeacherSerializer(teacher,many=True)
#         return Response(data=serialiser.data,status=status.HTTP_200_OK)
#
#     @swagger_auto_schema(request_body=TeacherSerializer)
#     def patch(self, request,pk):
#         teacher=get_object_or_404(Teacher,pk=pk)
#         serializer = TeacherSerializer(teacher,data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data={'success':True,'data':serializer.data}, status=status.HTTP_201_CREATED)
#
#     @swagger_auto_schema(request_body=TeacherSerializer)
#     def put(self, request,pk):
#         teacher = get_object_or_404(Teacher, pk=pk)
#         serializer = TeacherSerializer(teacher, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data={'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
#
#     def delete(self, request,pk):
#         teacher=get_object_or_404(Teacher,pk=pk)
#         teacher.delete()
#         return Response(data={'message':"Malumot o'chirildi"},status=status.HTTP_204_NO_CONTENT)


class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = request.data.get('user')
        user = User.objects.filter(pk=user_id).first()

        if not user:
            return Response({"message": "Bunday user topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        if not user.is_teacher:
            return Response({"message": "Bu user teacher emas!"}, status=status.HTTP_400_BAD_REQUEST)

        if Teacher.objects.filter(user=user).exists():
            return Response({"message": "Bunday o'qituvchi allaqachon mavjud!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)