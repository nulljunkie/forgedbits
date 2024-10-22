from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()

class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Online' if self.is_online else 'Offline'}"


class Chat(models.Model):
    alice = models.ForeignKey(User, related_name='alice', on_delete=models.CASCADE)
    bob = models.ForeignKey(User, related_name='bob', on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat between {self.alice.username} and {self.bob.username}"

    class Meta:
        unique_together = ('alice', 'bob')


    def clean(self):
        if self.alice == self.bob:
            raise ValidationError('A user cannot send a friend request to themselves.')
        # Sort the sender and receiver based on their IDs to avoid (alice, bob) and (bob, alice) as separate entries
        if self.alice.pk > self.bob.pk:
            self.alice, self.bob = self.bob, self.alice
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} at {self.timestamp}"
