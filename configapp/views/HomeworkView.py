from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import *
from ..serializers import *
from ..add_permission import *
from drf_yasg.utils import swagger_auto_schema


class GiveHomework(APIView):
    permission_classes = [IsTeacherPermission]
    @swagger_auto_schema(request_body=HomeworkSerializer)
    def post(self, request, group):
        groups = get_object_or_404(Group, id=group)
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(group=groups)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, group):
        grou = Homework.objects.filter(group__id=group)
        serializer = HomeworkSerializer(grou, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckHomework(APIView):
    permission_classes = [IsTeacherPermission]
    @swagger_auto_schema(request_body=CheckHomeworkSerializer)
    def put(self, request, group):
        homework = get_object_or_404(Homework, group=group)
        student_id = request.data.get("student")
        submission = get_object_or_404(HomeworkGet, homework=homework, student_id=student_id)
        serializer = CheckHomeworkSerializer(submission, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_submitted=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, group):
        submissions = HomeworkGet.objects.filter(
            homework__group__id=group,
            is_submitted=True
        )
        serializer = CheckHomeworkSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoHomework(APIView):
    permission_classes = [IsStudentPermission]
    @swagger_auto_schema(request_body=DoHomeworkSerializer)
    def post(self, request,hw=None):
        st=get_object_or_404(Students,user=request.user)
        serializer = DoHomeworkSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(student=st)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, hw):
        h1 = get_object_or_404(Homework, pk=hw)
        homework=HomeworkGet.objects.filter(homework=h1)
        serializer = DoHomeworkSerializer(homework,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
