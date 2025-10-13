from rest_framework import serializers
from ..models import News, NewsFotos
from configapp.models.auth_user import User  # kerak bo‘lsa qo‘shing

class NewsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFotos
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    images = NewsPhotoSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        author = validated_data.get('author')

        news = NewsFotos.objects.create(**validated_data)
        for image_data in images_data:
            NewsFotos.objects.create(news=news, **image_data)

        return news
