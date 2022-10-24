from django.urls import path
from . import views

urlpatterns = [
    path('', views.artists.as_view(), name="artists-home"),
    path('create/', views.artists_create.as_view(), name="artists-create")
]
