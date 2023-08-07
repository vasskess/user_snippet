from django.contrib.auth import admin as auth_admin
from django.contrib import admin
from django.contrib.auth import get_user_model

from user_snippet.helpers.get_profile_helper import get_profile_model

User = get_user_model()
profile_model = get_profile_model()


@admin.register(User)
class AppUserAdmin(auth_admin.UserAdmin):
    """
    Custom admin panel for the custom User model.

    This admin panel is used to manage and display custom User model instances
    in the Django admin interface.

    Attributes:
        model (User): The custom User model associated with this admin panel.
        list_display (tuple): The fields to display in the list view of the admin panel.
        fieldsets (tuple): The grouping of fields to display in the detail view of the admin panel.
        add_fieldsets (tuple): The fields to display when adding a new User instance.
        ordering (tuple): The default ordering for the list view of the admin panel.
    """

    model = User
    list_display = ("email", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ("email",)


admin.site.register(profile_model)
