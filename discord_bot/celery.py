from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discord_bot.settings')
app = Celery('discord_bot')
app.config_from_object('django.conf:settings')#, namespace='Celery')
app.autodiscover_tasks()
