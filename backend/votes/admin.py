from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Vote


class VoteInline(GenericTabularInline):
    model = Vote

admin.site.register(Vote)
