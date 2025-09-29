from rest_framework.viewsets import ModelViewSet
from ..add_permission import *
from ..models import *
from ..serializers import *


class ManagerOrganizationView(ModelViewSet):
    queryset = ManagerOrganization.objects.all()
    serializer_class = ManagerOrganizationSerializer
