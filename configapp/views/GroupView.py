from rest_framework.views import APIView
from ..serializers import *
from rest_framework.viewsets import ModelViewSet


class CrudGroupView(ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()


class CrudTableView(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()