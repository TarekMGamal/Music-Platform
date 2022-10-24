from django.shortcuts import render, redirect
from .forms import CreateAlbumForm
from django.views.generic import CreateView
from .models import Album

class albums_create(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/albums_create.html'
    success_url = '/artists/'