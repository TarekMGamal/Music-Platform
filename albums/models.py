from enum import auto
from unicodedata import decimal
from django.db import models
from artists.models import Artist

class Album(models.Model):
    name = models.CharField(max_length=100, default='New Album')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False, max_digits=9, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
