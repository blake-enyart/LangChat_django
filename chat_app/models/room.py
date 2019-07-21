from django.db import models
from .language import Language

class Room(models.Model):
    name = models.TextField(unique=True)
    # label = models.SlugField(unique=True)
    language = models.ForeignKey(Language,
            related_name='languages',
            on_delete=models.CASCADE,
            default=1
    )
