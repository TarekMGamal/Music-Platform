from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import user_serializer
from .models import User

class user_detail_api(generics.RetrieveUpdateAPIView):
    serializer_class = user_serializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    
    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)
    