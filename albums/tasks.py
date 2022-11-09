from celery import shared_task
from django.core.mail import send_mail
from music_platform.settings import DEFAULT_FROM_EMAIL

@shared_task
def send_email(artist, album):
    send_mail(
        subject = 'Congratulations',
        message = 'Hi {}, Congrats for publishing your new album {}'.format(artist.stage_name, album.name),
        recipient_list = [artist.email],
        fail_silently = False,
        from_email = DEFAULT_FROM_EMAIL
    )
    
    return