from workers.environment import config
from celery import Celery
import os
import logging

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
app = Celery('search', backend=config['CELERY_BACKEND'], broker=config['CELERY_BACKEND'])
app.conf.task_routes = {
    'c2.*': { 'queue': 'c2' },
    'api.*': { 'queue': 'api' },
    'search.*': { 'queue': 'search' }
}

app.autodiscover_tasks([
    'workers.splunk',
    'workers.system'
])
