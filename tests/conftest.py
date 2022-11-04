import pytest
from rest_framework.test import APIClient
from users.models import User

@pytest.fixture
def auth_client():
    def auth_client_function(user = None):
        client = APIClient()
        
        login_data = {
            "username": "",
            "password": ""
        }
        
        if (user == None):
            data = {
                "username": "testuser",
                "email": "testemail@something.com",
                "password": "Testpassword123",
                "confirm_password": "Testpassword123"
            }
            
            login_data["username"] = data["username"]
            login_data["password"] = data["password"]
            
            client.post('/accounts/register/', data)
        else:
            login_data["username"] = user.username
            login_data["password"] = user.password
                
        response = client.post('/accounts/login/', login_data)
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        return client
    
    return auth_client_function


@pytest.fixture
def non_auth_client():
    client = APIClient()
        
    return client