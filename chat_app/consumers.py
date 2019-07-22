from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from pprint import pprint as pp
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Room, User, Message, Language

import json

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_message(self, text_data_json):
        user = get_user_model().objects.get(id=text_data_json['user_id'])
        room = Room.objects.get(id=text_data_json['room_id'])
        if room:
            Message.objects.create(room=room, user=user, message=text_data_json['message'])
        else:
            room = Room.objects.create(
                name=text_data_json['message'],
                language=Language.objects.get(
                    id=text_data_json['language_id'])
            )
            Message.objects.create(room=room, user=user, message=text_data_json['message'])

        return Message.objects.last()

    async def connect(self):
        self.user = self.scope["user"]
        # pp(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        pp(self.scope)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        whole_message = await self.save_message(text_data_json)

        whole_message = json.dumps(whole_message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': whole_message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
