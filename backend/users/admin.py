from django.contrib import admin

from .models import Profile, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "birth_date", "is_active", "is_staff", "last_login", "date_joined"]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "image", "bio", "location", "website", "linkedin_profile", "github_profile", "phone_number"]

admin.site.register(Profile, ProfileAdmin)
