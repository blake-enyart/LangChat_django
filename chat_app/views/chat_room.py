from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework.response import Response
from ..models import Room
import json

def index(request):
    return render(request, 'chat_app/index.html', {})

def room(request, room_name):

    return render(request, 'chat_app/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user': request.user
    })

# def room(request, room_name):
#     room = Room.objects.get(name=room_name)
#
#     # We want to show the last 50 messages, ordered most-recent-last
#     messages = reversed(room.messages.order_by('-timestamp')[:50])
#     for idx, m in enumerate(messages):
#         md = model_to_dict(m)
#         messages[idx] = json.dumps(md, cls=DjangoJSONEncoder)
#
#     return Response({
#         'room_name_json': mark_safe(json.dumps(room_name)),
#         'messages_json': messages
#     })
