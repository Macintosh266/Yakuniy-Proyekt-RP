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


# class StudentView(APIView):
#     @swagger_auto_schema(request_body=StudentSerializer)
#     def post(self,request):

        

class StudentView(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = FAddStudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = request.data.get('user')
        user = User.objects.filter(pk=user_id).first()

        if not user:
            return Response({"message": "Bunday user topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        if not user.is_student:
            return Response({"message": "Bu user student emas!"}, status=status.HTTP_400_BAD_REQUEST)

        if Students.objects.filter(user=user).exists():
            return Response({"message": "Bunday o'quvchi allaqachon mavjud!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


