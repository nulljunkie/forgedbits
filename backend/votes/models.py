from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from posts.models import Post
from users.models import User


class Type(models.IntegerChoices):

    UPVOTE = 1
    DOWNVOTE = -1

class Vote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=Type.choices)

    # ContentType and object_id define the relationship to any model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return f"Vote by {self.user} on {self.content_object} with type {self.type}"
