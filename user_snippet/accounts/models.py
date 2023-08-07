from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify

from user_snippet.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_ERROR = "User with that email already exists !"

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name="Email",
        error_messages={"unique": USERNAME_ERROR},
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        default=False, null=False, blank=False, verbose_name="Staff status"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = "email"
    objects = AppUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    FIRST_NAME_MAX_LEN = 100
    LAST_NAME_MAX_LEN = 100

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="User email",
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name="Last Name",
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
        verbose_name="slug",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.email.split("@")[0])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email.split('@')[0]}"
