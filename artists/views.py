from django.shortcuts import redirect, render
from albums.models import Album
from .forms import CreateArtistForm


def artists(request):
    albums = Album.objects.select_related('artist').order_by('artist').all()
    data = {
        'albums': albums
    }
    return render(request, 'artists/artists.html', data)


def artists_create(request):
    if request.method == 'POST':
        form = CreateArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artists-home')
    else:
        form = CreateArtistForm()
        
    return render(request, 'artists/artists_create.html', {'form': form})