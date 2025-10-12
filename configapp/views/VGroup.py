from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from ..models import Students
from ..serializers import AddStudentSerializer, CheckSerializerStudent
from ..add_permission import IsAdminPermission

class CheckGroup(APIView):
    permission_classes=[IsAdminPermission]
    def get(self, request, pk):
        groups = Students.objects.filter(group=pk)
        serializer = AddStudentSerializer(groups, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CheckSerializerStudent(many=True))
    def patch(self, request, pk):
        students = Students.objects.filter(group=pk)
        if not students.exists():
            return Response({'detail': 'Hech qanday student topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CheckSerializerStudent(students, data=request.data, many=True, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        Students.objects.filter(group=pk).update(is_line=True)
        return Response({'success': True}, status=status.HTTP_200_OK)



