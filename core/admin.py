from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .admin_forms import UserAdminCreationForm, userAdminChangeForm

from django.contrib.auth import get_user_model

user = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to change and add user objects
    form = userAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("cellphone_number", "is_superuser", "is_shop_owner")
    list_filter = ("is_superuser", "is_staff", "is_shop_owner", "active")
    fieldsets = (
        ("personal info", {"fields": ("first_name", "last_name")}),
        (None, {"fields": ("cellphon_number", "email", "password")}),
        (
            "Permissions",
            {"fields": ("is_superuser", "is_shop_owner", "is_staff", "active")},
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("cellphone_number", "password1", "password2"),
            },
        ),
    )
    search_fields = ("cellphone_number", "first_name", "last_name")
    ordering = ("cellphone_number", "first_name", "last_name")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
