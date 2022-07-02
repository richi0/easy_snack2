import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Article, City, Country


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return Article.objects.filter(publish_on__lte=datetime.date.today())

    def lastmod(self, obj):
        return obj.updated_at


class CitySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return [i for i in City.objects.all() if i.is_in_published_article()]

    def lastmod(self, obj):
        return datetime.datetime.now()


class CountrySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return [i for i in Country.objects.all() if i.is_in_published_article()]

    def lastmod(self, obj):
        return datetime.datetime.now()


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return ["about", "map", "disclaimer", "blog_home","city_home", "country_home"]

    def location(self, item):
        return reverse(item)
