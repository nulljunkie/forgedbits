from django.conf import settings
from django.db import models
from posts.models import Post


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', related_name="replies", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content

    class Meta:
        ordering = ['created_at']

