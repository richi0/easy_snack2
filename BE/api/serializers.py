from rest_framework import serializers
from blog.models import Article, City


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id",
            "author",
            "title",
            "image",
            "caption",
            "restaurant_name",
            "cost",
            "country",
            "city",
            "google_map",
            "snacks",
            "preface",
            "publish_on",
        )


class ArticleDetailSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField("get_content")
    city_name = serializers.SerializerMethodField("get_city")
    country_name = serializers.SerializerMethodField("get_country")

    def get_content(self, obj):
        request = self.context.get("request")
        posts = [p.json() for p in obj.paragraphs.all()]
        images = [i.json(request) for i in obj.images.all()]
        return sorted(posts + images, key=lambda i: i["order"])

    def get_city(self, obj):
        return obj.city.name

    def get_country(self, obj):
        return obj.country.name

    class Meta:
        model = Article
        fields = (
            "content",
            "city_name",
            "country_name",
            "id",
            "author",
            "title",
            "image",
            "caption",
            "restaurant_name",
            "cost",
            "country",
            "city",
            "google_map",
            "snacks",
            "preface",
            "publish_on",
        )


class CityListSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField("get_country")
    posts = serializers.SerializerMethodField("get_posts")

    def get_country(self, obj):
        return obj.country.name

    def get_posts(self, obj):
        return len(obj.get_posts())

    class Meta:
        model = City
        fields = (
            "id",
            "image",
            "name",
            "description",
            "country",
            "country_name",
            "posts",
        )


class CityDetailSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField("get_country")
    articles = serializers.SerializerMethodField("get_articles")


    def get_country(self, obj):
        return obj.country.name

    def get_articles(self, obj):
        return [i.json() for i in obj.get_posts()]

    class Meta:
        model = City
        fields = ("id", "image", "name", "description", "country", "country_name", "articles")

class CountryListSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField("get_posts")

    def get_posts(self, obj):
        return len(obj.get_posts())

    class Meta:
        model = City
        fields = (
            "id",
            "image",
            "name",
            "description",
            "posts",
        )


class CountryDetailSerializer(serializers.ModelSerializer):
    cities = serializers.SerializerMethodField("get_cities")

    def get_cities(self, obj):
        return [i.json() for i in obj.get_cities()]

    class Meta:
        model = City
        fields = (
            "id",
            "image",
            "name",
            "description",
            "cities",
        )