from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin

from .models import SiteConfig


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
                    "bale_url",
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
