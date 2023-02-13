import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("flight_manager", broker="redis://localhost:6379")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "every_30_minutes": {
        "task": "flight_manager.flights.tasks.increment_flight_price",
        "schedule": crontab(minute=30),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
