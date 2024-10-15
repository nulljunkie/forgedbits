from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(source='sender.profile.image', read_only=True)

    class Meta:
        model = Notification
        exclude = ['user', 'sender']

