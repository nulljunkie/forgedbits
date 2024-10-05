from django.contrib import admin
from votes.admin import VoteInline

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'parent', 'created_at')
    list_filter = ('created_at', 'post', 'parent')
    search_fields = ('content',)
    ordering = ('-created_at',)
    inlines = [VoteInline]

admin.site.register(Comment, CommentAdmin)
