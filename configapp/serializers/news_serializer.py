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
        news = News.objects.create(**validated_data)

        # Avval rasmlar yaratamiz
        image_objs = []
        for image_data in images_data:
            image_obj = NewsFotos.objects.create(**image_data)
            image_objs.append(image_obj)

        # Keyin News bilan bog‘laymiz (ManyToMany uchun .set())
        news.images.set(image_objs)
        return news
