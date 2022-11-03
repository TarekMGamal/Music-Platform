import pytest
from tests.conftest import auth_client, non_auth_client
from artists.models import Artist


@pytest.mark.django_db
def test_artists_api(auth_client):
    client = auth_client()
    
    response = client.get('/artists/')
    
    response_data = response.data
    data = list(Artist.objects.all())

    assert response.status_code == 200
    assert data == response_data    
    

@pytest.mark.django_db
def test_artists_create(auth_client, non_auth_client):
    authenticated_client = auth_client()
    non_authenticated_client = non_auth_client
    
    data = {
        "stage_name": "testartist",
        "social_media_link": "https://www.instagram.com/"
    }
    
    response1 = authenticated_client.get('/artists/create/')
    response2 = non_authenticated_client.get('/artists/create/')
    response3 = authenticated_client.post('/artists/create/', data)
    
    assert response1.status_code == 200  # authenticated client should access this endpoint normaly
    assert response2.status_code == 302  # should redirect to login page
    assert response3.status_code == 302  # should create new artist and redirect to artists page