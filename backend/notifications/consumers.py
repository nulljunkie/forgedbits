import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):

    groups = []

    async def connect(self):

        if self.scope['user'].is_authenticated:

            self.channel_name = self.scope["user"].username
            self.groups.append(self.channel_name)

            print(self.channel_name)
            print(self.groups)

            # Add user to the group (each user has a unique channel group)
            await self.channel_layer.group_add(
                self.channel_name, 
                # 'imad',
                self.channel_name
            )

            await self.accept()

            # Send an immediate notification upon connecting
            await self.send(text_data=json.dumps({
                'notification': 'hello friend, that lame!'
            }))

            await self.channel_layer.group_send(
                self.channel_name,  
                # 'imad',
                {
                    'type': 'notify',  # This will trigger the `notify` method
                    'message': 'fucking idiot, you got this'  # The message content
                }
            )
            await self.send(text_data=json.dumps({
                'notification': 'shit didn\'t get the group_send!'
            }))

    async def disconnect(self, close_code):
        # Remove user from their channel group on disconnect
        await self.channel_layer.group_discard(
            self.channel_name,
            # 'imad',
            self.channel_name
        )

    async def notify(self, event):
        await self.send(text_data=json.dumps({
            'notification': event['message']
        }))
