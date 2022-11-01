import pytest
from rest_framework.test import APIClient
from users.models import User

@pytest.fixture
def auth_client():
    def auth_client_function(user = None):
        client = APIClient()
        
        if (user == None):
            user = User.objects.create(username="testusername", password="testpassword")
            
        client.force_login(user)

        return client
    
    return auth_client_function