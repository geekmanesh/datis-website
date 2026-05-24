# core/models.py
from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class SiteConfig(SingletonModel):
    """Global site configuration – only one instance exists."""

    company_name = models.CharField(max_length=255, verbose_name=_("Company name"))

    tagline = models.CharField(max_length=255, blank=True, verbose_name=_("Tagline"))

    logo = models.ImageField(
        upload_to="logos/", blank=True, null=True, verbose_name=_("Logo")
    )

    email = models.EmailField(blank=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone"))
    address = models.TextField(blank=True, verbose_name=_("Address"))
    working_hours = models.CharField(
        blank=True, max_length=500, verbose_name=_("Working hours")
    )

    bale_url = models.URLField(blank=True, verbose_name=_("Bale"))
    instagram_url = models.URLField(blank=True, verbose_name=_("Instagram"))
    linkedin_url = models.URLField(blank=True, verbose_name=_("LinkedIn"))

    hero_title = models.CharField(
        max_length=255, blank=True, verbose_name=_("Hero title")
    )

    hero_subtitle = models.TextField(blank=True, verbose_name=_("Hero subtitle"))

    hero_cta_text = models.CharField(
        max_length=100, blank=True, verbose_name=_("CTA button text")
    )

    hero_cta_link = models.CharField(
        max_length=255, blank=True, verbose_name=_("CTA link")
    )

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _("Site Configuration")

    def __str__(self):
        return self.company_name
