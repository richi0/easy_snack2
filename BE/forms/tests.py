from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CommentForm, ContactForm, SubscriptionForm
from .models import Comment, Contact, Subscription
from .views import CreateCommentView, CreateContactView, CreateSubscribeView
from blog.tests import create_blog_post
from blog.models import Article


class CreateCommentPageViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.pk = Article.objects.all()[0].pk
        self.response = self.client.post(
            reverse(
                "create_comment",
                kwargs={"pk": self.pk},
            ),
            {
                "name": "Test",
                "email": "test@test.com",
                "comment": "Test Comment TEST999#",
            },
        )

    def test_status_code_get(self):
        url = reverse(
            "create_comment",
            kwargs={"pk": self.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("blog_home"))

    def test_status_code_post_true(self):
        self.assertEqual(self.response.status_code, 200)

    def test_status_code_post_false(self):
        response = self.client.post(
            reverse(
                "create_comment",
                kwargs={"pk": self.pk},
            ),
            {
                "name": "Test",
                "email": "test@test.com",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("blog_detail", kwargs={"pk": self.pk}))

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "forms/thanks.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Snack")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("create_comment", kwargs={"pk": self.pk}))
        self.assertEqual(view.func.__name__, CreateCommentView.as_view().__name__)


class CreateCommentFormTests(TestCase):
    def test_form_field_label(self):
        form = CommentForm()
        self.assertTrue(form.fields["name"].label == "Name")
        self.assertTrue(form.fields["email"].label == "Email")
        self.assertTrue(form.fields["comment"].label == "Comment")

    def test_form_date_true(self):
        form = CommentForm(
            data={
                "name": "Test",
                "email": "test@test.com",
                "comment": "Test Comment TEST999#",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_date_false(self):
        form = CommentForm(
            data={
                "name": "Test",
                "email": "test@test.com",
                "comment": None,
            }
        )
        self.assertFalse(form.is_valid())


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_blog_post()

    def setUp(self):
        self.object = Comment.objects.all()[0]

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("name").verbose_name, "name")
        self.assertEqual(self.object._meta.get_field("email").verbose_name, "email")
        self.assertEqual(
            self.object._meta.get_field("created_at").verbose_name, "created at"
        )
        self.assertEqual(self.object._meta.get_field("comment").verbose_name, "comment")
        self.assertEqual(self.object._meta.get_field("article").verbose_name, "article")
        self.assertEqual(
            self.object._meta.get_field("approved").verbose_name, "approved"
        )

    def test_str(self):
        self.assertEqual(self.object.name, str(self.object))


class CreateContactPageViewTests(TestCase):
    def setUp(self):
        self.response = self.client.post(
            reverse("create_contact"),
            {
                "name": "Test",
                "email": "test@test.com",
                "message": "Test Comment TEST999#",
            },
        )

    def test_status_code_get(self):
        url = reverse("create_contact")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("about"))

    def test_status_code_post_true(self):
        self.assertEqual(self.response.status_code, 200)

    def test_status_code_post_false(self):
        response = self.client.post(
            reverse("create_contact"),
            {
                "name": "Test",
                "email": "test@test.com",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("about"))

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "forms/thanks.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Snack")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("create_contact"))
        self.assertEqual(view.func.__name__, CreateContactView.as_view().__name__)


class CreateContactFormTests(TestCase):
    def test_form_field_label(self):
        form = ContactForm()
        self.assertTrue(form.fields["name"].label == "Name")
        self.assertTrue(form.fields["email"].label == "Email")
        self.assertTrue(form.fields["message"].label == "Message")

    def test_form_date_true(self):
        form = ContactForm(
            data={
                "name": "Test",
                "email": "test@test.com",
                "message": "Test Comment TEST999#",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_date_false(self):
        form = ContactForm(
            data={
                "name": "Test",
                "email": "test@test.com",
                "message": None,
            }
        )
        self.assertFalse(form.is_valid())


class ContactModelTest(TestCase):
    def setUp(self):
        self.object = Contact.objects.create(
            name="Ylmaz",
            email="email2@example.com",
            message="This is the second comment TEST999#",
        )

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("name").verbose_name, "name")
        self.assertEqual(self.object._meta.get_field("email").verbose_name, "email")
        self.assertEqual(
            self.object._meta.get_field("created_at").verbose_name, "created at"
        )
        self.assertEqual(self.object._meta.get_field("message").verbose_name, "message")

    def test_str(self):
        self.assertEqual(self.object.name, str(self.object))


class CreateSubscriptionPageViewTests(TestCase):
    def setUp(self):
        self.response = self.client.post(
            reverse("create_subscription"),
            {
                "name": "Test",
                "email": "test@test.com",
            },
        )

    def test_status_code_get(self):
        url = reverse("create_subscription")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("subscribe"))

    def test_status_code_post_true(self):
        self.assertEqual(self.response.status_code, 200)

    def test_status_code_post_false(self):
        response = self.client.post(
            reverse("create_subscription"),
            {
                "name": "Test",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("subscribe"))

    def test_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "forms/thanks.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Snack")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No content")

    def test_view_class(self):
        view = resolve(reverse("create_subscription"))
        self.assertEqual(view.func.__name__, CreateSubscribeView.as_view().__name__)


class CreateSubscriptionFormTests(TestCase):
    def test_form_field_label(self):
        form = SubscriptionForm()
        self.assertTrue(form.fields["name"].label == "Name")
        self.assertTrue(form.fields["email"].label == "Email")

    def test_form_date_true(self):
        form = SubscriptionForm(
            data={
                "name": "Test",
                "email": "test@test.com",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_date_false(self):
        form = SubscriptionForm(
            data={
                "name": "Test",
                "email": None,
            }
        )
        self.assertFalse(form.is_valid())


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.object = Subscription.objects.create(
            name="Ylmaz",
            email="email2@example.com",
        )

    def test_labels(self):
        self.assertEqual(self.object._meta.get_field("name").verbose_name, "name")
        self.assertEqual(self.object._meta.get_field("email").verbose_name, "email")
        self.assertEqual(
            self.object._meta.get_field("created_at").verbose_name, "created at"
        )
        self.assertEqual(self.object._meta.get_field("url").verbose_name, "url")
        self.assertEqual(
            self.object._meta.get_field("subscribed").verbose_name, "subscribed"
        )

    def test_str(self):
        self.assertEqual(self.object.name, str(self.object))