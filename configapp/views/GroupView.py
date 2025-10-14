from rest_framework.views import APIView
from ..serializers import *
from rest_framework.viewsets import ModelViewSet
from ..add_permission import *

class CrudGroupView(ModelViewSet):
    permission_classes = [IsAdminPermission]
    serializer_class = GroupSerializers
    queryset = Group.objects.all()


class CrudTableView(ModelViewSet):
    permission_classes = [IsAdminPermission]
    serializer_class = TableSerializer
    queryset = Table.objects.all()