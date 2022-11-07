import pytest
from ..models import Album
from ..serializers import album_serializer
from artists.models import Artist
from users.models import User
from datetime import datetime

@pytest.mark.django_db
def test_album_serializer():
    test_user = User.objects.create(username='test user', password='testpassword123')
    test_artist = Artist.objects.create(stage_name='test artist', social_media_link='https://www.instagram.com/', user=test_user)
    album = Album.objects.create(name='test album', artist=test_artist, release_datetime=datetime(2001,5,5), cost=100.00)
    
    serializer = album_serializer(album)
    
    assert album.name == serializer.data['name']
    assert album.artist.id == serializer.data['artist']['id']
    assert str(album.release_datetime)[:10] == str(serializer.data['release_datetime'])[:10]
    assert album.cost == float(serializer.data['cost'])