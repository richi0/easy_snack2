from uuid import uuid4

from blog.models import Article
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


class Subscription(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subscribed = models.BooleanField(default=True)
    url = models.CharField(max_length=200, default=uuid4())
    created_at = models.DateTimeField(auto_now_add=True)

    def get_unsubscribe_url(self):
        return reverse("unsubscribe", kwargs={"slug": self.url})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
