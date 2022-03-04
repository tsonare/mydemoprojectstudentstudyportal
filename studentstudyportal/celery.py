import os
from celery import Celery
from celery import shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentstudyportal.settings')

app = Celery('studentstudyportal')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# CELERY_CACHE_BACKEND = 'default'

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@shared_task
def name_of_your_function(optional_param):
    pass 

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')