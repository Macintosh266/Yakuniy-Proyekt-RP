from django import views
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from configapp.serializers.email_seralizer import *
from configapp.models.auth_user import *
from rest_framework.response import Response
from django.core.mail import send_mail


class SendEmailView(APIView):
    @swagger_auto_schema(request_body=SendMassageSerializer)
    def post(self, request):
        serializer = SendMassageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.validated_data['email']
        cr=TimePassword.objects.create(email=email)


        full_message = f"""
        Sizga django tomonidan xabar yuborildi:
        password: {cr.time_password}
        """
        send_mail(
            message=full_message,
            from_email="mtosh662@gmail",
            recipient_list=[f"{email}"],  # Yuboriladigan email
        )


        return Response({"message": full_message}, status=status.HTTP_200_OK)
    

class ChackEmailView(APIView):
    @swagger_auto_schema(request_body=ChackMassageSerializer)
    def post(self,request):
        serializer=ChackMassageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.validated_data['email']
        password=serializer.validated_data['password']

        try:
            cr=TimePassword.objects.filter(email=email,time_password=password)
        except TimePassword.DoesNotExist:
            return Response({'error': 'Kod noto‘g‘ri yoki email topilmadi'}, status=status.HTTP_400_BAD_REQUEST)

        cr.is_bool=True
        cr.save()

        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
