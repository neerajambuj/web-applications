from __future__ import absolute_import, unicode_literals
from celery import shared_task
from chat.bot import run_bot
from celery import task
#from celery.decorators import task
@task(name = "run_bot_task")
def run_bot_task():
   return  run_bot()
