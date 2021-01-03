'''import os
from celery import Celery

task_serializer = 'json'

app = Celery('discord_bot')
app.conf.broker_url = os.environ.get('REDISTOGO_URL', 'redis://localhost:6379/0')
ACCEPT_CONTENT = ['json']
'''
