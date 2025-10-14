from  rest_framework import status,serializers
from configapp.models.groupsmodel import *

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rooms
        fields='__all__'

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TableType
        fields='__all__'


class TableSerializer(serializers.ModelSerializer):
    type=TableTypeSerializer()

    class Meta:
        model=Table
        fields='__all__'

    def create(self, validated_data):
        type_data = validated_data.pop("type")

        type_obj, _ = TableType.objects.get_or_create(**type_data)

        table = Table.objects.create(type=type_obj, **validated_data)
        return table


class GroupSerializers(serializers.ModelSerializer):
    # table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())

    class Meta:
        model=Group
        fields='__all__'

    # def create(self, validated_data):
        # table_data = validated_data.pop("table")
        # table_serializer = TableSerializer(data=table_data)
        # table_serializer.is_valid(raise_exception=True)
        # table = table_serializer.save()
        #
        # group = Group.objects.create(table=table, **validated_data)
        # return group

class UpdateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields=['is_started']
