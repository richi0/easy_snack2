from django.db import models
from django.urls import reverse
import datetime

SNACKS = [
    (0.0, 0.0),
    (0.5, 0.5),
    (1.0, 1.0),
    (1.5, 1.5),
    (2.0, 2.0),
    (2.5, 2.5),
    (3.0, 3.0),
    (3.5, 3.5),
    (4.0, 4.0),
    (4.5, 4.5),
    (5.0, 5.0),
]

AUTHORS = [("Amby", "Amby"), ("Sev", "Sev")]


class Article(models.Model):
    author = models.CharField(max_length=200, choices=AUTHORS, default="Amby")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/title_images/")
    caption = models.CharField(max_length=200, blank=True, null=True, default="")
    restaurant_name = models.CharField(max_length=200)
    cost = models.FloatField(default=0.0)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, null=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True)
    google_map = models.TextField(blank=True, null=True)
    snacks = models.FloatField(choices=SNACKS, default=0.0)
    preface = models.TextField(default="")
    sent_newsletter = models.BooleanField(default=False)
    publish_on = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.id)])

    def get_text(self):
        paragraps = self.paragraphs.all()
        images = self.images.all()
        text = list(paragraps) + list(images)
        return sorted(text, key=lambda obj: obj.order)

    def get_cords(self) -> tuple:
        if self.google_map and self.is_published:
            pos1 = self.google_map.find("!2d") + 3
            pos2 = self.google_map.find("!", pos1)
            pos3 = self.google_map.find("!3d") + 3
            pos4 = self.google_map.find("!", pos3)
            return (
                float(self.google_map[pos3:pos4]),
                float(self.google_map[pos1:pos2]),
            )
        else:
            return False

    @property
    def is_published(self):
        return datetime.date.today() >= self.publish_on

    class Meta:
        ordering = ["-created_at"]


class Paragraph(models.Model):
    type_ = "paragraph"
    title = models.CharField(max_length=200, blank=True, null=True, default="")
    content = models.TextField()
    article = models.ForeignKey(
        Article, related_name="paragraphs", on_delete=models.CASCADE
    )
    order = models.IntegerField(default=1)

    def json(self):
        return {
            "type_": self.type_,
            "title": self.title,
            "content": self.content,
            "article": self.article.id,
            "order": self.order,
        }

    def __str__(self):
        if self.title:
            return self.title
        else:
            if len(self.content) > 10:
                return self.content[:10]
        return self.content

    class Meta:
        ordering = ["order"]


class Image(models.Model):
    type_ = "image"
    image = models.ImageField(upload_to="uploads/article_images/")
    article = models.ForeignKey(
        Article, related_name="images", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=200, blank=True, null=True, default="")
    order = models.IntegerField()

    def json(self, request):
        return {
            "type_": self.type_,
            "image": request.build_absolute_uri(self.image.url),
            "caption": self.caption,
            "article": self.article.id,
            "order": self.order,
        }

    def __str__(self):
        if self.caption:
            return self.caption
        else:
            return str(self.image)

    class Meta:
        ordering = ["order"]


class City(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/places/")
    description = models.TextField()
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("city_detail", args=[str(self.id)])

    def get_posts(self):
        all_articles = Article.objects.filter(city=self)
        return [i for i in all_articles if i.is_published]

    def is_in_published_article(self):
        all_articles = self.get_posts()
        return any([i.is_published for i in all_articles])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cities"


class Country(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/countries/")
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("country_detail", args=[str(self.id)])

    def get_posts(self):
        all_articles = Article.objects.filter(country=self)
        return [i for i in all_articles if i.is_published]

    def get_cities(self):
        return City.objects.filter(country=self)

    def is_in_published_article(self):
        all_articles = self.get_posts()
        return any([i.is_published for i in all_articles])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "countries"
