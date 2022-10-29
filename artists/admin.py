from django.contrib import admin
from albums.models import Album
from .models import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'approved_albums_number')
    
    def approved_albums_number(self, artist_obj):
        approved_albums_number = Album.objects.filter(artist = artist_obj, is_approved = True).count()
        return approved_albums_number
        