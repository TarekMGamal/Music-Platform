from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Album(TimeStampedModel):
    name = models.CharField(max_length=100, default='New Album')
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False, max_digits=9, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
        
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='image/')
    image_thumbnail = ImageSpecField(source='image', format='JPEG')
    audio = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(['mp3', 'wav'])])
    
    def __str__(self):
        return self.name


@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, **kwargs):
    if instance.name == '':
        instance.name = instance.album.name
        
