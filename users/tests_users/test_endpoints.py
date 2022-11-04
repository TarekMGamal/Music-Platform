import pytest
from tests.conftest import auth_client, non_auth_client


@pytest.mark.django_db
def test_user_details_api(auth_client, non_auth_client):
    client = auth_client()
    
    response1 = client.get("/users/1")
    response2 = non_auth_client.get("/users/1")
    
    assert response1.status_code == 200
    assert response2.status_code == 401