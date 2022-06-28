from django.test import TestCase
from django.urls import resolve, reverse

from .views import AboutPageView, MapPageView, DisclaimerPageView, SubscriptionPageView


class AboutPageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("about")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "pages/about.html")
        self.assertTemplateUsed(self.response, "forms/components/form.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "About")
        self.assertContains(self.response, "Name")
        self.assertContains(self.response, "Email")
        self.assertContains(self.response, "Message")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("about"))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


class MapPageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("map")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "pages/map.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Map")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("map"))
        self.assertEqual(view.func.__name__, MapPageView.as_view().__name__)


class DisclaimerPageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("disclaimer")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "pages/disclaimer.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Disclaimer")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("disclaimer"))
        self.assertEqual(view.func.__name__, DisclaimerPageView.as_view().__name__)

class SubscribePageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("subscribe")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "pages/subscribe.html")
        self.assertTemplateUsed(self.response, "forms/components/form.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Subscribe")
        self.assertContains(self.response, "Name")
        self.assertContains(self.response, "Email")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("subscribe"))
        self.assertEqual(view.func.__name__, SubscriptionPageView.as_view().__name__)


class SitemapsPageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("sitemaps")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contains_correct_html(self):
        self.assertContains(self.response, "disclaimer")
        self.assertContains(self.response, "map")
        self.assertContains(self.response, "about")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")