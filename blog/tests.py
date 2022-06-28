import datetime

from django.test import TestCase
from django.urls import resolve, reverse

from forms.models import Comment
from .models import Article, Paragraph, Image, City, Country
from .views import (
    BlogHomePageView,
    BlogDetailView,
    CityHomePageView,
    CityDetailView,
    CountryHomePageView,
    CountryDetailView,
)


class BlogHomePageViewTests(TestCase):
    def setUp(self):
        create_blog_post()
        self.url = reverse("blog_home")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/blog_home.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Snack")
        self.assertContains(self.response, "Richie")
        self.assertContains(self.response, "title of article")
        self.assertContains(self.response, "https://example.com/image1.png")
        self.assertContains(self.response, "Just some text")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_not_published(self):
        date = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d").date()
        create_blog_post(author="Amby", title="Animals are cool", date=date)
        response = self.client.get(self.url)
        self.assertContains(response, "Amby")
        self.assertContains(response, "Animals are cool")
        date = datetime.datetime.strptime("2090-01-01", "%Y-%m-%d").date()
        create_blog_post(author="Sev", title="Otters are cool", date=date)
        response = self.client.get(self.url)
        self.assertNotContains(response, "Sev")
        self.assertNotContains(response, "Otters are cool")

    def test_view_class(self):
        view = resolve(reverse("blog_home"))
        self.assertEqual(view.func.__name__, BlogHomePageView.as_view().__name__)


class BlogDetailViewTests(TestCase):
    def setUp(self):
        self.blog_post = create_blog_post()
        self.url = self.blog_post.get_absolute_url()
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/blog_detail.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Richie")
        self.assertContains(self.response, "title of article")
        self.assertContains(self.response, "https://example.com/image1.png")
        self.assertContains(self.response, "Just some text")
        self.assertContains(self.response, "Paragraph1")
        self.assertContains(self.response, "This is the conten for the first paragraph")
        self.assertContains(self.response, "Paragraph2")
        self.assertContains(
            self.response, "This is the conten for the second paragraph"
        )
        self.assertContains(self.response, "Joe")
        self.assertContains(self.response, "Name")
        self.assertContains(self.response, "Price per Person:")
        self.assertContains(self.response, "Country")
        self.assertContains(self.response, "Snacks")
        self.assertContains(self.response, "this is a nice meal")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")
        self.assertNotContains(self.response, "Ylmaz")
        self.assertNotContains(self.response, "This is the second comment")

    def test_blog_detail_view_class(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, BlogDetailView.as_view().__name__)


class CityHomePageViewTests(TestCase):
    def setUp(self):
        create_blog_post()
        self.url = reverse("city_home")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/city_home.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Antigua")
        self.assertContains(self.response, "Guatemala")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("city_home"))
        self.assertEqual(view.func.__name__, CityHomePageView.as_view().__name__)


class CityDetailPageViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.url = City.objects.all()[0].get_absolute_url()
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/city_detail.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Antigua")
        self.assertContains(self.response, "Guatemala")
        self.assertContains(self.response, "I love Antigua!")
        self.assertContains(self.response, "https://example.com/antigua.png")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, CityDetailView.as_view().__name__)

class CountryHomePageViewTests(TestCase):
    def setUp(self):
        create_blog_post()
        self.url = reverse("country_home")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/country_home.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Guatemala")
        self.assertContains(self.response, "Number of Posts: 1")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("country_home"))
        self.assertEqual(view.func.__name__, CountryHomePageView.as_view().__name__)


class CityDetailPageViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.url = Country.objects.all()[0].get_absolute_url()
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/country_detail.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Antigua")
        self.assertContains(self.response, "Guatemala")
        self.assertContains(self.response, "Guatemala is great!")
        self.assertContains(self.response, "https://example.com/guatemala.png")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, CountryDetailView.as_view().__name__)

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.object = Article.objects.all()[0]

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("author").verbose_name, "author")
        self.assertEqual(self.object._meta.get_field("title").verbose_name, "title")
        self.assertEqual(self.object._meta.get_field("image").verbose_name, "image")
        self.assertEqual(self.object._meta.get_field("preface").verbose_name, "preface")
        self.assertEqual(
            self.object._meta.get_field("restaurant_name").verbose_name,
            "restaurant name",
        )
        self.assertEqual(self.object._meta.get_field("cost").verbose_name, "cost")
        self.assertEqual(self.object._meta.get_field("country").verbose_name, "country")
        self.assertEqual(
            self.object._meta.get_field("google_map").verbose_name, "google map"
        )
        self.assertEqual(self.object._meta.get_field("snacks").verbose_name, "snacks")
        self.assertEqual(
            self.object._meta.get_field("publish_on").verbose_name, "publish on"
        )
        self.assertEqual(
            self.object._meta.get_field("created_at").verbose_name, "created at"
        )
        self.assertEqual(
            self.object._meta.get_field("updated_at").verbose_name, "updated at"
        )

    def test_str(self):
        self.assertEqual(self.object.title, str(self.object))


class ParagraphModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.object = Paragraph.objects.all()[0]

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("title").verbose_name, "title")
        self.assertEqual(self.object._meta.get_field("content").verbose_name, "content")
        self.assertEqual(self.object._meta.get_field("article").verbose_name, "article")
        self.assertEqual(self.object._meta.get_field("order").verbose_name, "order")

    def test_str(self):
        self.assertEqual(self.object.title, str(self.object))


class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.object = Image.objects.all()[0]

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("image").verbose_name, "image")
        self.assertEqual(self.object._meta.get_field("caption").verbose_name, "caption")
        self.assertEqual(self.object._meta.get_field("article").verbose_name, "article")
        self.assertEqual(self.object._meta.get_field("order").verbose_name, "order")

    def test_str(self):
        self.assertEqual(self.object.caption, str(self.object))


class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.object = City.objects.all()[0]

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("name").verbose_name, "name")
        self.assertEqual(
            self.object._meta.get_field("description").verbose_name, "description"
        )
        self.assertEqual(self.object._meta.get_field("image").verbose_name, "image")
        self.assertEqual(self.object._meta.get_field("country").verbose_name, "country")

    def test_str(self):
        self.assertEqual(self.object.name, str(self.object))


class CountryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.object = Country.objects.all()[0]

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("name").verbose_name, "name")
        self.assertEqual(
            self.object._meta.get_field("description").verbose_name, "description"
        )
        self.assertEqual(self.object._meta.get_field("image").verbose_name, "image")

    def test_str(self):
        self.assertEqual(self.object.name, str(self.object))


        self.assertEqual(self.object.name, str(self.object))

def create_blog_post(
    author="Richie", title="title of article", date=datetime.date.today()
):
    country = Country.objects.create(
        name="Guatemala",
        image="https://example.com/guatemala.png",
        description="Guatemala is great!",
    )

    city = City.objects.create(
        name="Antigua",
        image="https://example.com/antigua.png",
        description="I love Antigua!",
        country=country,
    )
    article = Article.objects.create(
        author=author,
        title=title,
        image="https://example.com/image1.png",
        preface="Just some text",
        restaurant_name="Johnnys Bar",
        cost=22.1,
        country=country,
        city=city,
        google_map="this is fake",
        snacks=4.5,
        publish_on=date,
    )

    Paragraph.objects.create(
        title="Paragraph1",
        content="This is the conten for the first paragraph",
        article=article,
        order=1,
    )

    Paragraph.objects.create(
        title="Paragraph2",
        content="This is the conten for the second paragraph",
        article=article,
        order=2,
    )

    Image.objects.create(
        image="https://example.com/image1.png",
        caption="this is a nice meal",
        article=article,
        order=2,
    )

    Comment.objects.create(
        name="Joe",
        email="email@example.com",
        comment="This is the first comment TEST999#",
        article=article,
        approved=True,
    )

    # Not approved and will not show on the page
    Comment.objects.create(
        name="Ylmaz",
        email="email2@example.com",
        comment="This is the second comment TEST999#",
        article=article,
    )
    return article
