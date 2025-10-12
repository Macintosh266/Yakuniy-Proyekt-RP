from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from configapp.models.auth_user import *
from configapp.serializers.email_seralizer import LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from configapp.make_token import get_tokens_for_user

class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email'].lower()
        password = serializer.validated_data['password']

        user = User.objects.filter(email=email).first()

        # ✅ 1. Check if user exists
        if not user:
            return Response(
                {"success": False, "message": "Login ma'lumotlari noto‘g‘ri"},
                status=status.HTTP_401_UNAUTHORIZED
            )


        # ✅ 2. Check password
        if not user.check_password(password):
            return Response(
                {"success": False, "message": "Parol noto‘g‘ri"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ✅ 3. Check OTP if student
        if user.is_student:
            tp = TimePassword.objects.filter(email=email).first()
            if tp is None:
                return Response(
                    {"error": "Bu email uchun OTP yuborilmagan"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not tp.is_bool:
                return Response(
                    {"error": "Email OTP orqali tasdiqlanmagan"},
                    status=status.HTTP_400_BAD_REQUEST
                )


        # ✅ 4. Create and return tokens
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_200_OK)


