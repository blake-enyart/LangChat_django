from django.db import models

class Language(models.Model):
    name = models.TextField(blank=True)
    abbreviated_name = models.CharField(max_length=10)
