import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_platform.settings')

app = Celery('music_platform')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY_CONF' means all celery-related configuration keys
#   should have a `CELERY_CONF` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY_CONF')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

'''
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
'''