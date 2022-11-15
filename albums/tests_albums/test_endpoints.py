import pytest
from artists.models import Artist
from tests.conftest import auth_client, non_auth_client


@pytest.mark.django_db
def test_albums_create(auth_client, non_auth_client):
    authenticated_client = auth_client()
    non_authenticated_client = non_auth_client
    
    test_artist = Artist.objects.create(stage_name='test', social_media_link='https://www.instagram.com')
    data = {
        "name": "testalbum",
        "artist": test_artist,
        "release_datetime": "12/12/2001",
        "cost": 100.0,
        "is_approved": True
    }
    
    response1 = authenticated_client.get('/albums/create/')
    response2 = non_authenticated_client.get('/albums/create/')
    response3 = authenticated_client.post('/albums/create/', data)
    
    assert response1.status_code == 200  # authenticated client should access this endpoint normaly
    assert response2.status_code == 302  # should redirect to login page
    assert response3.status_code == 200  # should create new album and redirect to artists page