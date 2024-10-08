from django.conf import settings
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-posts_count']

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover = models.ImageField(blank=True, null=True, upload_to="post-covers/")
    views_count = models.PositiveIntegerField(blank=True, null=True)
    viewer = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='viewers')
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
