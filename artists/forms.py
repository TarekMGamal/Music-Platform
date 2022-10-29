from dataclasses import fields
from django.forms import ModelForm
from .models import Artist

class CreateArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['stage_name', 'social_media_link']