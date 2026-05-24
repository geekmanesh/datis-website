import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode
from django.utils.text import slugify


class ProjectCategory(models.Model):
    name = models.CharField(
        max_length=120,
        blank=False,
        null=False,
        verbose_name=_(
            "Category name",
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Project(models.Model):

    class StatusChoices(models.TextChoices):
        DONE = "done", _("Done")
        IN_PROGRESS = "in-progress", _("In Progress")

    id = models.UUIDField(
        primary_key=True, blank=False, null=False, default=uuid.uuid4, db_index=True
    )
    slug = models.SlugField(unique=True, blank=True, editable=False)

    name = models.CharField(
        max_length=400, blank=False, null=False, verbose_name=_("Project name")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )
    client = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_("Client")
    )
    cost = models.PositiveBigIntegerField(verbose_name=_("Cost"))
    category = models.ForeignKey(
        ProjectCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        verbose_name=_("Category"),
    )

    status = models.TextField(
        null=False,
        blank=False,
        choices=StatusChoices.choices,
        default=StatusChoices.IN_PROGRESS,
        verbose_name=_("Status"),
    )

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            ascii_name = unidecode(self.name)
            base_slug = slugify(ascii_name)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Project"),
    )
    image = models.ImageField(upload_to="project_images/", verbose_name=_("Image"))

    def __str__(self):
        image_name = self.image.name.split("/")[-1]
        return f"Image: {image_name}"

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Project Images")
