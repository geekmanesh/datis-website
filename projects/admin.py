from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Project, ProjectCategory, ProjectImage
from .forms import ProjectForm


class ProjectImageInline(admin.TabularInline):  # or StackedInline
    model = ProjectImage
    extra = 1
    max_num = 4
    min_num = 0


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    form = ProjectForm
    list_display = ["name", "category", "customer", "status"]
    inlines = [ProjectImageInline]
    exclude = ["id"]
    fieldsets = (
        (
            "Basic Information",
            {"fields": ("name", "description", "category")},
        ),
        (
            "Client & Financial",
            {"fields": ("customer", "cost")},
        ),
        (
            "Status",
            {"fields": ("status",)},
        ),
    )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    pass
