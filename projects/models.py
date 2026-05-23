import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


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
        IN_PROGRESS = "in-progress", _("In-progress")

    id = models.UUIDField(
        primary_key=True, blank=False, null=False, default=uuid.uuid4, db_index=True
    )
    name = models.CharField(
        max_length=400, blank=False, null=False, verbose_name=_("Project name")
    )
    description = models.TextField(verbose_name=_("Description"))
    status = models.TextField(
        null=False,
        blank=False,
        choices=StatusChoices.choices,
        default=StatusChoices.IN_PROGRESS,
        verbose_name=_("Status"),
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
