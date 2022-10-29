from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.albums_create.as_view(), name="albums-create")
]
