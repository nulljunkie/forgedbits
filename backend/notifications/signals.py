from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification


@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:

        # Get the channel layer
        channel_layer = get_channel_layer()

        # print('channel_layer': channel)

        async_to_sync(channel_layer.group_send)(
            instance.user.username,  # channel of owner of this notification
            {
                'type': 'notify',
                'message': instance.message
            }
        )
