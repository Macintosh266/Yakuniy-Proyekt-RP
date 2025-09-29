from rest_framework import serializers
from ..models import *

class ManagerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ManagerOrganization
        fields='__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields='__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields='__all__'