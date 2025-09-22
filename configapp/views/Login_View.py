from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from configapp.models.auth_user import User
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
        
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.filter(email=email).first()
        if not user:
            return Response(
                data={"success": False, "message": "Login ma'lumotlari noto'g'ri"},
                status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response(data={'success': False, 'message': "Parol noto'g'ri"}, status=status.HTTP_400_BAD_REQUEST)
        

        
        token = get_tokens_for_user(user)

        return Response(data=token, status=status.HTTP_200_OK)