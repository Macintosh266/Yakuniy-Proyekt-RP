from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from sqlparse.engine.grouping import group
from ..add_permission import *
from ..models import *
from ..serializers import *


class CheckGroup(APIView):
    def get(self,request,pk):
        groups=Students.objects.filter(group=pk)
        serializer=AddStudentSerializer(groups,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


    def patch(self,request,pk):
        groups=Students.objects.filter(group=pk)
        serializer=AddStudentSerializer(groups,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self,request,pk):
        groups=Students.objects.filter(group=pk)
        serializer=AddStudentSerializer(groups,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)