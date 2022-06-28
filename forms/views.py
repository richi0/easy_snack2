from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse

from .forms import ContactForm, CommentForm, SubscriptionForm
from blog.models import Article
from .helpers.mail import new_contact_mail, new_comment_mail

class CreateContactView(View):
    def get(self, request):
        return redirect("about")

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            new_contact_mail(obj)
            return render(
                request,
                "forms/thanks.html",
                {
                    "text": "Thank you for contacting us; we will respond as soon as possible."
                },
            )
        return redirect("about")

class CreateCommentView(View):
    def get(self, request, pk):
        return redirect("blog_home")

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            article = Article.objects.get(pk=pk)
            obj = form.save(commit=False)
            obj.article = article
            obj.save()
            new_comment_mail(obj, article)
            return render(
                request,
                "forms/thanks.html",
                {
                    "text": "Thanks for your comment. We will publish it as soon as possible."
                },
            )
        return redirect(reverse("blog_detail", args=[pk]))

class CreateSubscribeView(View):
    def get(self, request):
        return redirect("subscribe")

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "forms/thanks.html",
                {
                    "text": "Thank you for the subscription."
                },
            )
        return redirect("subscribe")