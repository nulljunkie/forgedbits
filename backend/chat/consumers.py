import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from .serializers import MessageSerializer

User = get_user_model()
from .models import Chat, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']

        query_string = dict((x.split('=') for x in self.scope['query_string'].decode().split('&')))
        chat_id = query_string.get('chat_id', None)
        
        if not(self.user.is_authenticated and chat_id):
            await self.close(code=40101)
        self.chat = await get_chat(chat_id)
        if self.chat is None:
            await self.close(code=40404)
        if self.user not in (self.chat.alice, self.chat.bob):
            await self.close(code=40404)

        self.group_name = f'chat_{chat_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print('data :', data)
        sender = data.get('sender', None)
        if not sender:
            return
        sender_instance = await get_user(sender)
        message = data.get('message', None)
        if sender_instance and message:
            if (self.chat):
                message_instance = await create_message(self.chat, sender_instance, message)
                if message_instance:
                    serializer = MessageSerializer(message_instance)
                    await self.channel_layer.group_send(self.group_name, {
                        'type': 'send_message',
                        'message': serializer.data
                    })


    async def send_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
        }))


@database_sync_to_async
def get_chat(id):
    try: 
        return Chat.objects.prefetch_related('alice', 'bob').get(pk=id)
    except Chat.DoesNotExist:
        return None


@database_sync_to_async
def create_message(chat, sender, message):
    if (chat):
        return Message.objects.create(chat=chat, sender=sender, message=message)
    return None

@database_sync_to_async
def get_user(username):
    try: 
        return User.objects.get(pk=username)
    except User.DoesNotExist:
        return None

