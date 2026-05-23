from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Project, ProjectCategory, ProjectImage
from .forms import ProjectForm
from django.utils.translation import gettext_lazy as _


class ProjectImageInline(admin.TabularInline):  # or StackedInline
    model = ProjectImage
    extra = 1
    max_num = 4
    min_num = 0


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    form = ProjectForm
    list_display = ["name", "category", "client", "status"]
    inlines = [ProjectImageInline]
    exclude = ["id"]
    fieldsets = (
        (
            _("Basic Information"),
            {"fields": ("name", "description", "category")},
        ),
        (
            _("Client & Financial"),
            {"fields": ("client", "cost")},
        ),
        (
            _("Status"),
            {"fields": ("status",)},
        ),
    )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
