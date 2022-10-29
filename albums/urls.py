from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.albums_create, name="albums-create")
]
