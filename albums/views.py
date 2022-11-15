from django.shortcuts import render, redirect
from .forms import CreateAlbumForm
from django.views.generic import CreateView
from .models import Album
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, pagination, permissions, response
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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = albums_filter
    
    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)
        
        
class albums_manual_filter(generics.ListCreateAPIView):
    queryset = Album.objects.filter(is_approved=True)
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = album_serializer
    
    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)
        
    def list(self, request):
        cost_greater_than_equal = request.GET.get('cost__gte', 0)
        cost_less_than_equal = request.GET.get('cost__lte', 999999999.99)
        name_contains = request.GET.get('name__icontains', '')
        
        queryset = self.get_queryset()
        queryset = queryset.filter(cost__gte=cost_greater_than_equal, 
                                   cost__lte=cost_less_than_equal, 
                                   name__icontains=name_contains)
        
        serializer = album_serializer(queryset, many=True)
        data = serializer.data
        
        return response.Response(data)
