from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from rest_framework import permissions, generics
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from users.serializers import register_user_serializer

class create_user_api(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = register_user_serializer
    
    
class login_user_api(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request, user)
        
        temp_list = super(login_user_api, self).post(request, format=None)
        temp_list.data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'bio': user.bio
        }
        
        return temp_list