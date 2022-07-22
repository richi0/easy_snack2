from django.urls import path
from .views import *

urlpatterns = [
    path('article/', ArticleList.as_view(), name='api_article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='api_article_detail'),
    path('city/', CityList.as_view(), name='api_city_list'),
    path('city/<int:pk>/', CityDetail.as_view(), name='api_city_detail'),
    path('country/', CountryList.as_view(), name='api_country_list'),
    path('country/<int:pk>/', CountryDetail.as_view(), name='api_country_detail'),
]