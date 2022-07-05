from rest_framework import serializers
from blog.models import Article
import json


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

    def get_content(self, obj):
        posts = [p.json() for p in obj.paragraphs.all()]
        images = [i.json() for i in obj.images.all()]
        return json.dumps(sorted(posts + images, key=lambda i: i["order"]))

    class Meta:
        model = Article
        fields = (
            "content",
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
