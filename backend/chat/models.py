from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Online' if self.is_online else 'Offline'}"


class ActiveChat(models.Model):
    alice = models.ForeignKey(User, related_name='alice', on_delete=models.CASCADE)
    bob = models.ForeignKey(User, related_name='bob', on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat between {self.alice.username} and {self.bob.username}"

    class Meta:
        unique_together = ('alice', 'bob')


class ChatMessage(models.Model):
    chat = models.ForeignKey(ActiveChat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} at {self.timestamp}"
