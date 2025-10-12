from rest_framework.viewsets import ModelViewSet
from ..add_permission import *
from ..models import News,NewsFotos
from ..serializers import NewsSerializer,NewsPhotoSerializer

class NewsViews(ModelViewSet):
    permission_classes = [IsNewsPermission]
    queryset = News.objects.all()
    serializer_class =NewsSerializer

# class NewsPhotoViews(ModelViewSet):
#     permission_classes = [IsNewsPermission]
#     queryset = NewsFotos.objects.all()
#     serializer_class = NewsPhotoSerializer