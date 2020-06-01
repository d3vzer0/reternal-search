import os

config = {
    'CELERY_BACKEND': os.getenv('RT_CELERY_BACKEND', 'redis://localhost:6379'),
    'CELERY_BROKER': os.getenv('RT_CELERY_BACKEND', 'redis://localhost:6379'),
    'CELERY_TIMER': os.getenv('RT_CELERY_TIMER', 10.0),
    'SPLUNK_TOKEN': os.getenv('RT_SPLUNK_TOKEN'),
    'SPLUNK_HOST': os.getenv('RT_SPLUNK_HOST', 'localhost'),
    'SPLUNK_PORT': os.getenv('RT_SPLUNK_PORT', 8089),
    'SPLUNK_APP': os.getenv('RT_SPLUNK_APP', 'search')
}

routes = {
    'agent.*': {
        'queue': os.getenv('AGENT_QUEUE', 'agent')
    },
    'api.*': {
        'queue': os.getenv('API_ROUTE', 'api')
    },
    'c2.*': {
        'queue': os.getenv('C2_ROUTE', 'c2')
    },
    'search.*': {
        'queue': os.getenv('SEARCH_ROUTE', 'search')
    }
}
