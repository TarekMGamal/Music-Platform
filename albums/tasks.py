from celery import shared_task
from django.core.mail import send_mail
from music_platform.settings import DEFAULT_FROM_EMAIL

@shared_task
def send_email(artist_name, album_name):
    send_mail(
        subject = 'Congratulations',
        message = 'Hi {}, Congrats for publishing your new album {}'.format(artist_name, album_name),
        recipient_list = [DEFAULT_FROM_EMAIL],
        fail_silently = False,
        from_email = DEFAULT_FROM_EMAIL
    )
    
    return