from django.shortcuts import redirect, render
from albums.models import Album
from .models import Artist
from .forms import CreateArtistForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import artist_serializer

class artists(TemplateView):
    template_name = 'artists/artists.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['albums'] = Album.objects.select_related('artist').order_by('artist').all()
        return context


class artists_create(LoginRequiredMixin, CreateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = 'artists/artists_create.html'
    success_url = '/artists/'
    

# REST framework views

class artists_api(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = artist_serializer