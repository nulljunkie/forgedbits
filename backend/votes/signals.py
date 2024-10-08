from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification

from .models import Vote


@receiver(post_save, sender=Vote)
def create_notification(sender, instance, created, **kwargs):
    if created:
        if instance.type == 1:

            # user who voted
            voter = instance.user.username

            # user who will receive the notification
            notification_receiver = instance.content_object.author

            content = str(instance.content_object)
            subject = str(instance.content_type.name)

            message = f'{voter} liked your {subject} \"{content}\"'
            print(notification_receiver.username, '<==', message)

            Notification.objects.create(user=notification_receiver, message=message)
