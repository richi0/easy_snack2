from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import BlogSitemap, StaticSitemap, CitySitemap, CountrySitemap

sitemaps = {
    "blog": BlogSitemap,
    "static": StaticSitemap,
    "city": CitySitemap,
    "country": CountrySitemap,
}

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # Local apps
    path("", include("blog.urls")),
    path("", include("pages.urls")),
    path("api/", include("api.urls")),
    path("froms/", include("forms.urls")),
    # Sitemaps
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemaps",
    ),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
