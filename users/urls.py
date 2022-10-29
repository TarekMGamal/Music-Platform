from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.user_detail_api.as_view(), name='user-detail')
]