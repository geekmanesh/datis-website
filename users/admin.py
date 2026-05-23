from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group


@admin.register(User)
class ProjectAdmin(ModelAdmin):
    list_display = ["full_name", "email", "is_superuser"]
    exclude = ["id", "last_login"]
    fieldsets = (
        (
            _("Basic Information"),
            {
                "fields": (
                    "full_name",
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Permissions"),
            {"fields": ("user_permissions",)},
        ),
        (
            _("Status"),
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )


admin.site.unregister(Group)
