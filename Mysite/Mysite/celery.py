import os
from celery import Celery
import platform

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mysite.settings")
app = Celery("Mysite")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

if platform.system() == "Windows":
    app.conf.worker_pool = "solo"