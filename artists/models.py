from django.db import models

class Artist(models.Model):
    stage_name = models.CharField(max_length=100, unique=True, blank=False)
    social_media_link = models.URLField(max_length=500, blank=True, null=False)
    
    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
    