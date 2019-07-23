from .models import Room, User, Message, Language
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

import json

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_message(self, text_data_json):
        user = self.scope['user']
        room = Room.objects.get(id=text_data_json['room_id'])
        reference_message = Message.objects.filter(id=text_data_json['reference'])
        if not room:
            room = Room.objects.create(
                name=text_data_json['message'],
                language=Language.objects.get(id=text_data_json['language_id'])
            )
        if len(reference_message):
            Message.objects.create(room=room, user=user,
                message=text_data_json['message'], reference=reference_message.first()
            )
            rm = reference_message.first()
        else:
            Message.objects.create(room=room, user=user,
                message=text_data_json['message']
            )
            rm = None
        return [Message.objects.latest('timestamp'), rm]

    async def connect(self):
        user = self.scope["user"]
        if user.is_anonymous:
            await self.close()
        else:
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
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        m, rm = await self.save_message(text_data_json)
        whole_message = model_to_dict(m)

        if type(rm) == Message:
            rm = model_to_dict(rm)
        user = self.scope['user']
        whole_message['username'] = user.username
        whole_message['reference'] = rm
        whole_message = json.dumps(whole_message, cls=DjangoJSONEncoder) # for dt conversion
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': whole_message,

            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
