import datetime
from blog.models import Article
from rest_framework import pagination, generics

from .serializers import *


class SmallPagination(pagination.PageNumberPagination):
    page_size = 8
    max_page_size = 8
    page_query_param = "p"
    page_size_query_param = "page_size"


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.filter(publish_on__lte=datetime.date.today()).order_by(
        "-publish_on", "created_at"
    )
    serializer_class = ArticleListSerializer
    pagination_class = SmallPagination


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
