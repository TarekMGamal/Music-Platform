from rest_framework import serializers
from .models import Album
from artists.serializers import artist_serializer

class album_serializer(serializers.ModelSerializer):
    artist = artist_serializer(read_only=True)
    
    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release_datetime', 'cost']
