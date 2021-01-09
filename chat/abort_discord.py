from celery import Celery
from itertools import chain
from discord_bot.celery import app
from schedular.models import Tasks
from billiard.exceptions import Terminated
from schedular.tasks import discord_app_task
import sys
import traceback
import celery

def abort_discord_app():
    try:
        app_task = Tasks.objects.all()
        print("Revoke Initiated")
        l = len(app_task)
        print("l=")
        print(app_task)
        # Killing the running tasks using sigkill system call
        for ids in app_task:
            app.control.revoke(ids.task_id, terminate=True, signal='SIGKILL')
            ids.delete()
        print("Done")
    except:
        print(sys.exc_info())
        print(traceback.print_exception(*sys.exc_info()))
        print(traceback.format_exc())

   
 
