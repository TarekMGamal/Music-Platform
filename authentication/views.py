from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from users.serializers import user_serializer


class create_user_api(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = user_serializer