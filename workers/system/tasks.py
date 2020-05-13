from celery.schedules import crontab
from workers import app
from yaml import Loader
import yaml

available_workers = []
with open('workers/config.yaml') as config_file:
    available_workers = yaml.load(config_file.read(), Loader=Loader)
    
@app.task(name='search.system.workers')
def get_workers() -> list:
    ''' Return list of plugins/workers '''
    return available_workers


@app.task(name='search.system.state')
def get_states(worker_name):
    ''' Placeholder, should return state of worker '''
    if not worker_name in available_workers: return { 'states':{ } }
    return available_workers
