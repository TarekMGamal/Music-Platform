from rest_framework import serializers
from .models import Artist

class artist_serializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'stage_name', 'social_media_link']
