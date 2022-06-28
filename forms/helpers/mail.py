import os

from django.template.loader import render_to_string
from mailjet_rest import Client

API_KEY = os.environ["MJ_APIKEY_PUBLIC"]
API_SECRET = os.environ["MJ_APIKEY_PRIVATE"]
mailjet = Client(auth=(API_KEY, API_SECRET), version="v3.1")


def new_comment_mail(comment, article):
    emails = os.environ["ADMIN_EMAIL"].split(",")
    names = os.environ["ADMIN_NAME"].split(",")
    to = [{"Email": email, "Name": names[i]} for i, email in enumerate(emails)]
    message = f"New comment on https://easy-snack.com{article.get_absolute_url()}\n\n"
    message += f"Name: {comment.name}\n"
    message += f"Email: {comment.email}\n"
    message += f"Comment: {comment.comment}\n"
    send_mail(to, message, "New comment on Easy-Snack")


def new_contact_mail(contact):
    emails = os.environ["ADMIN_EMAIL"].split(",")
    names = os.environ["ADMIN_NAME"].split(",")
    to = [{"Email": email, "Name": names[i]} for i, email in enumerate(emails)]
    message = "New contact on https://easy-snack.com/about/\n\n"
    message += f"Name: {contact.name}\n"
    message += f"Email: {contact.email}\n"
    message += f"Message: {contact.message}\n"
    send_mail(to, message, "New contact on Easy-Snack")


def subscription_mail(subscribers, articles):
    data = {"Messages": []}
    for subscriber in subscribers:
        data["Messages"].append(
            {
                "From": {"Email": "info@easy-snack.com", "Name": "Easy-Snack Blog"},
                "To": [{"Email": subscriber.email, "Name": subscriber.name}],
                "Subject": "Easy-Snack Weekly Update",
                "HTMLPart": render_to_string(
                    "forms/subscription_mail.html",
                    {"subscriber": subscriber, "articles": articles},
                ),
            }
        )
    mailjet.send.create(data=data)


def send_mail(to, message, subject):
    data = {
        "Messages": [
            {
                "From": {"Email": "info@easy-snack.com", "Name": "Easy-Snack Blog"},
                "To": to,
                "Subject": subject,
                "TextPart": message,
            }
        ]
    }
    if "TEST999#" in message:
        # Does not send mails if tests are run
        lines = message.split("\n")
        print(f"New mail: {lines[-2]}")
    else:
        mailjet.send.create(data=data)
