from django.db import models
from .room import Room
from .user import User
from django.utils import timezone

class Message(models.Model):
    room = models.ForeignKey(Room,
        related_name='messages',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User,
        related_name='messages',
        on_delete=models.CASCADE
    )
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ('-timestamp',)
