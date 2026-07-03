from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin

from .models import ContactMessage, SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(ModelAdmin, SingletonModelAdmin):
    list_display = ("company_name", "company_name", "email", "phone")

    fieldsets = (
        (
            _("Basic Information"),
            {
                "fields": (
                    "company_name",
                    "tagline",
                    "logo",
                )
            },
        ),
        (
            _("Contact Details"),
            {
                "fields": (
                    "email",
                    "phone",
                    "address",
                    "working_hours",
                )
            },
        ),
        (
            _("Social Media"),
            {
                "fields": (
                    "telegram_url",
                    "instagram_url",
                    "linkedin_url",
                )
            },
        ),
        (
            _("Homepage Hero Section"),
            {
                "fields": (
                    "hero_title",
                    "hero_subtitle",
                    "hero_cta_text",
                    "hero_cta_link",
                )
            },
        ),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ("name", "phone", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "phone", "message")
    readonly_fields = ("name", "phone", "message", "ip_address", "created_at")
    actions = ["mark_as_read", "mark_as_unread"]

    def has_add_permission(self, request):
        return False

    @admin.action(description=_("Mark selected messages as read"))
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description=_("Mark selected messages as unread"))
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
