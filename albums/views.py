from django.shortcuts import render, redirect
from .forms import CreateAlbumForm

def albums_create(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artists-home')
    else:
        form = CreateAlbumForm()
        
    return render(request, 'albums/albums_create.html', {'form': form})