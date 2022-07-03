import json
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render

from blog.models import Article
from forms.forms import ContactForm, SubscriptionForm
from forms.models import Subscription


class ConstructionPageView(TemplateView):
    template_name = "pages/construction.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context


class SubscriptionPageView(TemplateView):
    template_name = "pages/subscribe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SubscriptionForm()
        return context


class UnsubscriptionPageView(View):
    template_name = "pages/subscribe.html"

    def get(self, *args, **kwargs):
        sub = Subscription.objects.filter(url=kwargs["slug"])
        if len(sub):
            sub = sub[0]
            sub.subscribed = False
            sub.save()
            return render(
                self.request,
                "forms/thanks.html",
                {
                    "text": "You unsubscribed succesfully."
                },
            )
        else:
            return render(
                self.request,
                "forms/thanks.html",
                {
                    "text": "No subscriber with this url."
                },
            )


class MapPageView(TemplateView):
    template_name = "pages/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["markers"] = self.marker_string(Article.objects.all())
        return context

    @staticmethod
    def marker_string(posts):
        markers = []
        for post in posts:
            pos = post.get_cords()
            if pos:
                markers.append(
                    {
                        "pos": [pos[0], pos[1]],
                        "url": f'<a href="{post.get_absolute_url()}">{post.title}</a>',
                    }
                )

        return json.dumps(markers)


class DisclaimerPageView(TemplateView):
    template_name = "pages/disclaimer.html"

def test1(request):
    return HttpResponse('{"test1": "this is a test"}')