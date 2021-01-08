from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discord_bot.settings')
#os.environ.get('REDISTOGO_URL', 'redis://localhost:6379/0')
#os.environ.get('REDISTOGO_URL','redis://redistogo:59000e2261216b9b34c63b7eadab022a@crestfish.redistogo.com:11012/')
app = Celery('discord_bot')
app.config_from_object('django.conf:settings')#, namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))
