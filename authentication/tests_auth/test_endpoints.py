import pytest
from tests.conftest import auth_client, non_auth_client
from users.models import User

@pytest.mark.django_db
def test_create_user_api(auth_client, non_auth_client):    
    data1 = {
        "username": "testuser1",
        "email": "testemail1@something.com",
        "password": "testpassword12345",
        "confirm_password": "testpassword12345"
    }
    data2 = {
        "username": "testuser2",
        "email": "testemail2@something.com",
        "password": "testpassword12345",
        "confirm_password": "testpassword12345"
    }
    data3 = {
        "username": "testuser1",
        "email": "testemail3@something.com",
        "password": "testpassword12345",
        "confirm_password": "testpassword12345"
    }
    data4 = {
        "username": "testuser3",
        "email": "testemail4@something.com",
        "password": "testpassword12345",
        "confirm_password": "testpassword1234"
    }
    data5 = {
        "username": "testuser4",
        "email": "testemail5@something.com",
        "password": "12345",
        "confirm_password": "12345"
    }
    data6 = {
        "username": "testuser5",
        "email": "123456789",
        "password": "testpassword12345",
        "confirm_password": "testpassword12345"
    }
    
    auth_client1 = auth_client()
    
    response1 = non_auth_client.post('/accounts/register/', data1)
    response2 = auth_client1.post('/accounts/register/', data2)
    response3 = non_auth_client.post('/accounts/register/', data3)
    response4 = non_auth_client.post('/accounts/register/', data4)
    response5 = non_auth_client.post('/accounts/register/', data5)
    response6 = non_auth_client.post('/accounts/register/', data6)
    
    
    user1 = User.objects.filter(username=data1["username"]).first()
    assert user1.username == data1["username"]
    
    assert response1.status_code == 201  # non authenticated user should access this endpoint normaly
    assert response2.status_code == 201  # authenticated user should access this endpoint normaly
    assert response3.status_code == 400  # should not create user with already used username
    assert response4.status_code == 400  # password & confirm password should be equal
    assert response5.status_code == 400  # password should be strong
    assert response6.status_code == 400  # email should be valid
    
    
    
@pytest.mark.django_db
def test_login_user_apis(non_auth_client):
    data1 = {
        "username": "testuser1",
        "email": "testemail1@something.com",
        "password": "testpassword12345",
        "confirm_password": "testpassword12345"
    }
    data2 = {
        "username": "testuser1",
        "password": "testpassword12345"
    }
    
    response_register_1 = non_auth_client.post('/accounts/register/', data1)
    response_login_1 = non_auth_client.post('/accounts/login/', data2)

    assert response_register_1.status_code == 201  # user should be registered
    assert response_login_1.status_code == 200  # user should be authenticated