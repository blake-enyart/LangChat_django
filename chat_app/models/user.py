from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    country_of_origin = models.TextField()
