from django.urls import path
from . import views
from django_filters.views import FilterView

urlpatterns = [
    path('create/', views.albums_create.as_view(), name="albums-create"),
    path('', views.albums.as_view(), name="albums"),
    path('filter/', FilterView.as_view(filterset_class=views.albums_filter)),
    path('filter/manual/', views.albums_manual_filter.as_view()),
]
