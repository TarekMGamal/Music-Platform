from django.db import models
from artists.models import Artist
from django.utils import timezone

class Album(models.Model):
    name = models.CharField(max_length=100, default='New Album')
    creation_datetime = models.DateTimeField(default=timezone.now(), editable=False)
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False, max_digits=9, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
