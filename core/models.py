from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.utils import OperationalError, ProgrammingError
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    message = models.TextField(
        blank=True,
        validators=[
            MaxLengthValidator(1000, message="پیام شما باید کمتر از ۱۰۰۰ کاراکتر باشد")
        ],
        verbose_name=_("Message"),
    )

    ip_address = models.GenericIPAddressField(
        null=True, blank=True, verbose_name=_("IP address")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent at"))
    is_read = models.BooleanField(default=False, verbose_name=_("Read"))

    class Meta:
        verbose_name = _("Contact message")
        verbose_name_plural = _("Contact messages")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.phone})"


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

    telegram_url = models.URLField(blank=True, verbose_name=_("Telegram"))
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

    @classmethod
    def load(cls):
        try:
            return cls.get_solo()
        except OperationalError, ProgrammingError:
            # Table not migrated yet (e.g. first run before `migrate` has
            # been applied). Fall back to an unsaved default instance so
            # pages that render site_config don't hard-crash.
            return cls()

    def __str__(self):
        return self.company_name
