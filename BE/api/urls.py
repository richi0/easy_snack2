from django.urls import path
from .views import *

urlpatterns = [
    path('article/', ArticleList.as_view(), name='api_article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='api_article_detail'),
]