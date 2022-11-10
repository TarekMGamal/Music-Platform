from celery import shared_task
from django.core.mail import send_mail
from music_platform.settings import DEFAULT_FROM_EMAIL
from datetime import datetime, timedelta
from artists.models import Artist
from django.db.models import Q
from music_platform.celery import app


@shared_task
def send_email(artist_name, artist_email, album_name):
    send_mail(
        subject = 'Congratulations',
        message = 'Hi {}, Congrats for publishing your new album {}'.format(artist_name, album_name),
        recipient_list = [artist_email],
        fail_silently = False,
        from_email = DEFAULT_FROM_EMAIL
    )
    
    return


@app.task
def daily_task():
    '''startdate = datetime.now()
    enddate = startdate + timedelta(days=30)
    
    artists_list = list(Artist.objects.all().select_related('album'))
    for artist in artists_list:
        latest_album = artist.album_set.latest('created_datetime') if artist.album_set.all().count() > 0 else None
        if latest_album == None or latest_album not in range(startdate, enddate):
            send_mail(
                subject = "Inactivity",
                message = "Hi {}, Your inactivity is causing their popularity on our platform to decrease".format(artist.stage_name),
                recipient_list = [artist.user.email],
                fail_silently = False,
                from_email = DEFAULT_FROM_EMAIL,
            )
    '''
    
    print('heeeloooooo')
    
    return
