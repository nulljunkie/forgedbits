from django.contrib import admin
from votes.admin import VoteInline

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'views_count', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content',)
    ordering = ('-created_at', )
    inlines = [VoteInline]

admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
