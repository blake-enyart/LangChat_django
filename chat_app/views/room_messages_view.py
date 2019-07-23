from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
# from django.utils.safestring import mark_safe
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Room
import json

class RoomMessageList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, room_id, format=None):
        room = Room.objects.get(id=room_id)

        # We want to show the last 50 messages, ordered most-recent-last
        messages = list(room.messages.order_by('-timestamp')[:50])
        for idx, m in enumerate(messages):
            user = messages.user
            md = model_to_dict(m)
            messages[idx] = md
            messages[idx]['username'] = user.username

        messages = list(reversed(messages))
        return Response(json.dumps(messages, cls=DjangoJSONEncoder))
