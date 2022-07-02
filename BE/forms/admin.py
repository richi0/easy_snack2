from django.contrib import admin
from .models import Contact, Subscription


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "created_at")
    ordering = ("-created_at",)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("name", "email", "url", "subscribed")
    ordering = ("-created_at",)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscription, SubscriptionAdmin)