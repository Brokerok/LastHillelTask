import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finishtask.settings')

app = Celery('finishtask')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every-day-update-orders': {
        'task': 'update_orders',
        'schedule': crontab(minute=0, hour=0)
    },
}

app.conf.beat_schedule = {
    'every-day-check-telegram': {
        'task': 'massage_to_telegram',
        'schedule': crontab(minute=10, hour=9)
    },
}
