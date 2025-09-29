from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..add_permission import *
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status

class AttendanceView(ModelViewSet):
    permission_classes = [IsNewsPermission]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer



class AttendanceLevelView(APIView):
    def get(self,request,pk):
        level=AttendanceLevel.objects.filter(pk=pk)
        serializer=AttendanceLevelSerializer(level,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
