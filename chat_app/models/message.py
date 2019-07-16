from django.db import models
from .room import Room
from django.utils import timezone

class Message(models.Model):
    room = models.ForeignKey(Room,
        related_name='messages',
        on_delete=models.CASCADE,
    )
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
