from django.shortcuts import render, redirect
from .forms import CreateAlbumForm
from django.views.generic import CreateView
from .models import Album
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, pagination, permissions
from .serializers import album_serializer
from django_filters import rest_framework as filters


class albums_create(LoginRequiredMixin, CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/albums_create.html'
    success_url = '/artists/'
    
    
class albums_filter(filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'cost': ['lte', 'gte'],
            'name': ['icontains'],
        }
    
    
class albums(generics.ListCreateAPIView):
    queryset = Album.objects.filter(is_approved=True)
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = album_serializer
    
    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)