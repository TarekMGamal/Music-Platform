# Task1
#### create some artists
    >>> from artists.models import Artist
    >>> artist1 = Artist(stage_name='Eminem', social_media_link='https://www.instagram.com/eminem/')
    >>> artist1.save()
    >>> artist2 = Artist(stage_name='Ludovico Einaudi', social_media_link='https://www.instagram.com/ludovico_einaudi/')
    >>> artist2.save()
    >>> artist3 = Artist(stage_name='The Weekend', social_media_link='https://www.instagram.com/theweeknd/')
    >>> artist3.save()
  
#### list down all artists
    >>> Artist.objects.all()
    <QuerySet [<Artist: Eminem>, <Artist: Ludovico Einaudi>, <Artist: The Weekend>]>

#### list down all artists sorted by name
    >>> Artist.objects.order_by('stage_name')
    <QuerySet [<Artist: Eminem>, <Artist: Ludovico Einaudi>, <Artist: The Weekend>]>

#### list down all artists whose name starts with  `a`
    >>> Artist.objects.filter(stage_name__startswith='a')
    <QuerySet []>

#### in 2 different ways, create some albums and assign them to any artists
    from datetime import datetime
    # way 1
	>>> album1 = Album(artist = artist1, name = "relapse", release_datetime = datetime(2009, 5, 15, 0, 0, 0), cost = 100.0)
    >>> album1.save()

	# way 2
    >>> artist3.album_set.create(name = "dawn fm", release_datetime = datetime(2022, 1, 7, 0, 0, 0), cost = 99.99)

#### get the latest released album
	>>> Album.objects.latest('release_datetime')
    <Album: Album object (2)>

#### get all albums released before today
    >>> Album.objects.filter(release_datetime__date__lt = datetime.today())
    <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>

#### get all albums released today or before but not after today
    >>> Album.objects.filter(release_datetime__date__lte = datetime.today())
    <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>

#### count the total number of albums (hint: count in an optimized manner)
    >>> Album.objects.all().count()
    2

#### in 2 different ways, for each artist, list down all of his/her albums
    # way 1
    >>> [artist.album_set.all() for artist in Artist.objects.all()]
    [<QuerySet [<Album: Album object (1)>]>, <QuerySet []>, <QuerySet [<Album: Album object (2)>]>]

    # way 2
    >>> [Album.objects.filter(artist_id=artist.id) for artist in Artist.objects.all()]
    [<QuerySet [<Album: Album object (1)>]>, <QuerySet []>, <QuerySet [<Album: Album object (2)>]>]

#### list down all albums ordered by cost then by name (cost has the higher priority)
    >>> Album.objects.order_by('cost', 'name')
    <QuerySet [<Album: Album object (2)>, <Album: Album object (1)>]>
