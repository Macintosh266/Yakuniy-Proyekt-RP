from rest_framework import serializers
from ..models import News,NewsFotos

class NewsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewsFotos
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    images=NewsPhotoSerializer()
    class Meta:
        model=News
        fields='__all__'