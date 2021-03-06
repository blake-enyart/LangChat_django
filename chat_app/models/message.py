from django.db import models
from django.utils import timezone
from .room import Room
from .user import User

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
    reference = models.ForeignKey('self',
        related_name='referenced_message',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-timestamp',)
