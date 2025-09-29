from rest_framework import serializers
from ..models import News,NewsFotos

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'


class NewsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewsFotos
        fields='__all__'