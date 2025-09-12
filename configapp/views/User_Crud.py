from configapp.models.auth_user import User
from configapp.models.studentsmodel import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from configapp.serializers.user_seralizer import UserSerializer   

class UserView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer=UserSerializer(users, many=True)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)
