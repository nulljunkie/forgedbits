import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from .models import ActiveChat, ChatMessage, UserStatus


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = f'chat_{self.user.id}'
        self.room_group_name = f'chat_{self.user.id}'

        # Join the room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Set user online status
        user_status, created = await database_sync_to_async(UserStatus.objects.get_or_create)(user=self.user)
        user_status.is_online = True
        await database_sync_to_async(user_status.save)()

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Set user offline status
        user_status = await database_sync_to_async(UserStatus.objects.get)(user=self.user)
        user_status.is_online = False
        await database_sync_to_async(user_status.save)()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        receiver_id = text_data_json['receiver_id']

        # Get or create the chat
        receiver = await database_sync_to_async(User.objects.get)(id=receiver_id)
        chat, created = await database_sync_to_async(ActiveChat.objects.get_or_create)(
            user1=self.user,
            user2=receiver
        )

        # Create and save the chat message
        chat_message = ChatMessage(chat=chat, sender=self.user, message=message)
        await database_sync_to_async(chat_message.save)()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
