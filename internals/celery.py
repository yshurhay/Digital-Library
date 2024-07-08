from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import dotenv
from pathlib import Path
path_to_env = Path(__file__).parents[1].joinpath(".env")

dotenv.load_dotenv(dotenv_path=path_to_env)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

app = Celery('django_api')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.conf.task_routes = [
    {'*': {'queue': os.environ['CELERY_DEFAULT_QUEUE']}}
]

app.autodiscover_tasks()
