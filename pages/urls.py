from django.urls import path
from .views import AboutPageView, DisclaimerPageView, MapPageView, SubscriptionPageView, UnsubscriptionPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('disclaimer/', DisclaimerPageView.as_view(), name='disclaimer'),
    path('map/', MapPageView.as_view(), name='map'),
    path('subscribe/', SubscriptionPageView.as_view(), name='subscribe'),
    path('unsubscribe/<slug:slug>/', UnsubscriptionPageView.as_view(), name='unsubscribe'),
]