from django.urls import path
from .views import (
    BlogHomePageView,
    BlogDetailView,
    CityHomePageView,
    CityDetailView,
    CountryHomePageView,
    CountryDetailView,
)

urlpatterns = [
    path("", BlogHomePageView.as_view(), name="blog_home"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("city/", CityHomePageView.as_view(), name="city_home"),
    path("city/<int:pk>/", CityDetailView.as_view(), name="city_detail"),
    path("country/", CountryHomePageView.as_view(), name="country_home"),
    path("country/<int:pk>/", CountryDetailView.as_view(), name="country_detail"),
]
