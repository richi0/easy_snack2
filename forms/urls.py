from django.urls import path
from .views import CreateContactView, CreateCommentView, CreateSubscribeView

urlpatterns = [
    path("contact/", CreateContactView.as_view(), name="create_contact"),
    path(
        "create_subscribe/", CreateSubscribeView.as_view(), name="create_subscription"
    ),
    path(
        "create_comment/<int:pk>/", CreateCommentView.as_view(), name="create_comment"
    ),
]