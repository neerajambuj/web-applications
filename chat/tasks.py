from __future__ import absolute_import, unicode_literals
from celery import shared_task
from chat.bot import run_bot
from celery.decorators import task
@shared_task(name = "run_bot_task")
def run_bot_task():
   print("jh")
   return  run_bot()
#def run_bot(x,y):
#    return x+y
