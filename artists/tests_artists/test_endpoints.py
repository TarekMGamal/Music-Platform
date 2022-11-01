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
    
    response1 = authenticated_client.get('/artists/create/')
    response2 = non_authenticated_client.get('/artists/create/')
    
    assert response1.status_code == 200
    assert response2.status_code == 302