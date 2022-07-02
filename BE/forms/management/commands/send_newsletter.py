import datetime

from blog.models import Article
from django.core.management.base import BaseCommand
from forms.helpers.mail import subscription_mail
from forms.models import Subscription


class Command(BaseCommand):
    help = "Sends a weekly newsletter with all new articles to all subscribers"
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    @staticmethod
    def set_articles_sent_true(articles):
        for article in articles:
            article.sent_newsletter = True
            article.save()

    def handle(self, *args, **options):
        subscribers = Subscription.objects.filter(subscribed=True)
        articles = Article.objects.filter(sent_newsletter=False)
        self.set_articles_sent_true(articles)
        if len(articles):
            subscription_mail(subscribers, articles)
            print(f"{self.date_time} Sent newsletter to {len(subscribers)} subscribers")
        else:
            print("No new articles this week.")
