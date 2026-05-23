from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Staff"))

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
