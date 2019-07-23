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
