
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devpulse_backend.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
