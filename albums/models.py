from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel

class Album(TimeStampedModel):
    name = models.CharField(max_length=100, default='New Album')
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False, max_digits=9, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
