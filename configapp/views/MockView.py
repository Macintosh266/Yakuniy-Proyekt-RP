import datetime
from calendar import month
from venv import create
from django.db.models.functions import TruncMonth
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ..add_permission import *
from ..models import *
from django.db.models import Count, Q
from rest_framework.response import Response
from ..serializers import *

class StudentMonthMock(APIView):
    # permission_classes = [IsAuthenticated,IsAdminPermission]
    def get(self, request,year):
        students = Students.objects.filter(created_at__year=year).annotate(month=TruncMonth('created_at')).values(
            'month').annotate(count=Count('id')).values(
            'month', 'count')
        student_data = {
            "data": students
        }
        return Response(data=student_data)



class DataMock(APIView):
    # permission_classes = [IsAuthenticated,IsAdminPermission]
    def get(self,request,date1,date2):
        student_true=Students.objects.filter(Q(created_at__gte=date1) & Q(created_at__lte=date2) & Q(
        user__is_active=True)).annotate(month=TruncMonth('created_at')).values(
        'month').annotate(count=Count('id')).values(
        'month', 'count')

        student_false = Students.objects.filter(Q(created_at__gte=date1) & Q(created_at__lte=date2) & Q(
            user__is_active=False)).annotate(month=TruncMonth('created_at')).values(
            'month').annotate(count=Count('id')).values(
            'month', 'count')

        student_data = {
            "comming_students": student_true,
            "not_comming_students":student_false,
        }
        return Response(data=student_data)




class SecondDataMock(APIView):
    # permission_classes = [IsAuthenticated,IsAdminPermission]
    def get(self, request, date1, date2):
        student_true = Students.objects.filter(Q(created_at__gte=date1) & Q(created_at__lte=date2) & Q(
            is_finish=True)).annotate(month=TruncMonth('created_at')).values(
            'month').annotate(count=Count('id')).values(
            'month', 'count')

        student_false = Students.objects.filter(Q(created_at__gte=date1) & Q(created_at__lte=date2) & Q(
            is_finish=False)).annotate(month=TruncMonth('created_at')).values(
            'month').annotate(count=Count('id')).values(
            'month', 'count')

        student_data = {
            "finishing_students": student_true,
            "not_finishing_students": student_false,
        }

        return Response(data=student_data)