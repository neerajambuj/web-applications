import os


task_serializer = 'json'


broker_url = os.environ.get('REDISTOGO_URL', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
