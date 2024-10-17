from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Chat, Message

User = get_user_model()

class ChatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="pk", read_only=True)
    alice = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    bob = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
