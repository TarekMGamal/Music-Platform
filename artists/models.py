from django.db import models
from django.db.models import Count, Q
from users.models import User

class ArtistManager(models.Manager):
    def get_queryset(self):
        approved_albums_number = Count('album', filter=Q(album__is_approved = True))
        return super().get_queryset().annotate(approved_albums = approved_albums_number)

class Artist(models.Model):
    stage_name = models.CharField(max_length=100, unique=True, blank=False)
    social_media_link = models.URLField(max_length=500, blank=True, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = ArtistManager()
    
    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
    