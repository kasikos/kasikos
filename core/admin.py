from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()
from .models import UserProfile

from .forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the Account model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "first_name",
        "last_name",
        "email",
        "cellphone_no",
        "last_login",
        "is_superuser",
    )
    list_filter = (
        "is_shopowner",
        "is_superuser",
        "is_staff",
        "active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "cellphone_no", "preferred_name",)}),
        ("Permissions", {"fields": ("is_shopowner", "is_superuser", "is_staff", "active",)}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. AccountAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
