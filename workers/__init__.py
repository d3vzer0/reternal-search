from workers.environment import config
from celery import Celery
import os
import logging

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
app = Celery('c2', backend=config['CELERY_BACKEND'], broker=config['CELERY_BACKEND'])
app.conf.task_routes = {
    'c2.*': { 'queue': 'c2' },
    'api.*': { 'queue': 'api' }    
}

app.autodiscover_tasks([
    'workers.empire2',
    'workers.system'
])

app.conf.beat_schedule = {
    'check-running-scenarios': {
        'task': 'c2.system.scheduler',
        'schedule': config['CELERY_TIMER'],
    }
}