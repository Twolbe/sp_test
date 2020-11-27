from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PlatformUser
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@admin.register(PlatformUser)
class PlatformUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("password1", "password2"),},),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email")
    ordering = []
