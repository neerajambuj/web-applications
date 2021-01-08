from celery import Celery
from itertools import chain
from discord_bot.celery import app
from schedular.models import Tasks
from billiard.exceptions import Terminated
from schedular.tasks import discord_app_task


@app.task(throws=(Terminated,))
def abort_discord_app():
    #print(celery.events)#.state.tasks_by_type(run_bot_task))
    #chat = Celery('discord_bot')
    try:
        app_task = Tasks.objects.all()
        print("Revoke Initiated")
        l = len(app_task)
        if l>1:
            for ids in app_task:
                try:
                    app.control.revoke(ids.task_id, terminate=True, signal='SIGUSR1')#'SIGKILL')
                except:
                    return None
                l -= 1
                if l==1:
                    break

            print("Done")
        else:
            #Just to avoid exceptions on server side and leaving one worker always running
            print("Done")
    except:
        print("Problem Encountered While Invoking")
    #for schedules in chain.from_iterable(app.control.inspect().scheduled().itervalues()):
    #    print(schedules)
    #chat.control.revokei
    #print(
    #[scheduled["request"]["id"] for scheduled in
    # chain.from_iterable(chat.control.inspect().scheduled()
    #                         .itervalues())])
    
 
