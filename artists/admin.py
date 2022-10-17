from django.contrib import admin

from albums.models import Album
from .models import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'get_approved_albums_number')
    
    def get_approved_albums_number(self, artist_obj):
        approved_albums_number = Album.objects.filter(artist = artist_obj, isApproved = True).count()
        return approved_albums_number
        