import uuid

from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Project(models.Model):

    class StatusChoices(models.TextChoices):
        DONE = "done", "Done"
        PENDING = "pending", "PENDING"

    id = models.UUIDField(
        primary_key=True, blank=False, null=False, default=uuid.uuid4, db_index=True
    )
    name = models.CharField(max_length=400, blank=False, null=False)
    description = models.TextField()
    status = models.TextField(
        null=False,
        blank=False,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    customer = models.CharField(max_length=200, null=False, blank=False)
    cost = models.PositiveBigIntegerField()
    category = models.ForeignKey(
        ProjectCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        image_name = self.image.name.split("/")[-1]
        return f"Image: {image_name}"

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Project Images"
