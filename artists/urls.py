from django.urls import path
from . import views

urlpatterns = [
    path('', views.artists, name="artists-home"),
    path('create/', views.artists_create, name="artists-create")
]
