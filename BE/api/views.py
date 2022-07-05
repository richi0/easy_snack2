from rest_framework import generics
from blog.models import Article

from .serializers import *


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
