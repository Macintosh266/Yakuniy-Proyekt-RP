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


class AttendanceGroupView(APIView):
    permission_classes = [IsTeacherPermission]
    def get(self,request,group):
        atten=Attendance.objects.filter(group=group)
        serializer=AttendanceSerializer(atten,many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=AttendanceSerializer)
    def post(self,request,group=None):
        serializer=AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)



class AttendanceLevelView(ModelViewSet):
    permission_classes = [IsAdminPermission]
    queryset = AttendanceLevel.objects.all()
    serializer_class = AttendanceLevelSerializer


