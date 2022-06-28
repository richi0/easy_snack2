from django import forms
from django.forms import ModelForm

from .models import Contact, Comment, Subscription


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Message"}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "comment"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "comment": forms.Textarea(attrs={"placeholder": "Comment"}),
        }


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
        }