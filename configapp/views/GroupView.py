from rest_framework.views import APIView
from configapp.serializers.groupseralizer import *
from configapp.models.groupsmodel import *
from rest_framework.viewsets import ModelViewSet


class CrudGroupView(ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()
