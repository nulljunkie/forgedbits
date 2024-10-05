import re

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from posts.models import Post

from .exceptions import WeakPasswordError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def validate_password(self, password: str):
        if password.__len__() >= 8:
            if bool(re.search(r"[!@#$%^&*(),.?\"\':{}|<>[\]\/\\~`+=-]", password)):
                if bool(re.search(r"\W", password)):
                    if bool(re.search(r"[0-9]", password)):
                        if bool(re.search(r"[A-Z]", password)):
                            return make_password(password)
        raise WeakPasswordError("password is weak")

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")

        user = self.model(username=username, password=password, **extra_fields)
        user.password = self.validate_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    username = models.CharField(
        _("username"),
        primary_key=True,
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[UnicodeUsernameValidator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
    )
    banner = models.ImageField(
        upload_to="profile_banners/",
        blank=True,
        null=True,
    )
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    github_profile = models.URLField(null=True, blank=True)
    saved_post = models.ManyToManyField(Post, related_name="saved_posts", blank=True)
    follower = models.ManyToManyField('self', symmetrical=False, related_name='followers',  blank=True)

    def __str__(self):
        return 'profile: ' + self.user.username
