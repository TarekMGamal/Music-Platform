from django.shortcuts import render
from albums.models import Album

def artists(request):
    albums = Album.objects.select_related('artist').order_by('artist').all()
    data = {
        'albums': albums
    }
    return render(request , 'artists/artists.html', data)