from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models
from django.utils.translation import gettext_lazy as _
from .models import Service, ServiceImage


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 0
    max_num = 4
    min_num = 1
    fields = ["image"]
    verbose_name = _("Gallery image")
    verbose_name_plural = _("Gallery images")


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("name", "order", "slug")
    list_editable = ("order",)
    search_fields = ("name",)
    exclude = ["slug"]
    inlines = [ServiceImageInline]
    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget},
    }

    fieldsets = (
        (
            _("Basic information"),
            {
                "fields": (
                    "name",
                    "short_description",
                    "order",
                    "content",
                )
            },
        ),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("images")
