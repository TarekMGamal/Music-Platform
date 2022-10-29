from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_user_api.as_view())
]