from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(blank=True, max_length=256)

    def __str__(self):
        return self.USERNAME_FIELD