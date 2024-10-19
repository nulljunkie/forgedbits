from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import Profile

from .models import Chat, Message

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = ['image', 'username']

class ChatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="pk", read_only=True)
    alice = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    bob = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = '__all__'

    def get_user(self, obj):
        me = self.context['request'].user
        user = obj.alice if obj.bob == me else obj.bob
        profile = Profile.objects.get(user=user)
        serializer = UserSerializer(profile)
        return serializer.data



class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


