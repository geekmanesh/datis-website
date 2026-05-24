# services/models.py
import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name=_("Service name"))
    short_description = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Short description"),
        help_text=_("Shown on the services listing page (approx. 50 characters)."),
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name=_("Order"), help_text=_("Lower number appears first.")
    )
    slug = models.SlugField(unique=True, blank=True, editable=False)

    content = models.TextField(
        blank=True,
        verbose_name=_("Content"),
        help_text=_(
            "Rich text with lists, ticks, font sizes – use the WYSIWYG editor."
        ),
    )

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            ascii_name = unidecode(self.name)
            base_slug = slugify(ascii_name)
            slug = base_slug
            counter = 1
            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServiceImage(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Service"),
    )
    image = models.ImageField(upload_to="service_gallery/", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Gallery image")
        verbose_name_plural = _("Gallery images")

    def __str__(self):
        return f"Image for {self.service.name}"
