from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from configapp.serializers.teacher_seralizer import *
from rest_framework.viewsets import ModelViewSet
from configapp.models.auth_user import *
from ..add_permission import *
from configapp.serializers.email_seralizer import *

class RegisterTeacher(APIView):
    @swagger_auto_schema(request_body=FTeacherSerializer)
    def post(self,request):
        serializer=FTeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data.get('user')
        email=user['email']

        tp = TimePassword.objects.filter(email=email).first()
        if tp is None:
            return Response(
                {"error": "Bu email uchun OTP yuborilmagan"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if tp.is_bool==False:
            return Response({"error": "Email OTP orqali tasdiqlanmagan"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        tp.delete()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class TeacherView(ModelViewSet):
    permission_classes = [IsAuthenticated,IsTeacherPermission]
    queryset = Teacher.objects.all()
    serializer_class = AddTeacherSerializer


