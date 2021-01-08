from celery import Celery
from itertools import chain
from discord_bot.celery import app
from schedular.models import Tasks
def abort_discord_app():
    #print(celery.events)#.state.tasks_by_type(run_bot_task))
    #chat = Celery('discord_bot')
    app_task = Tasks.objects.all()
    #app_id = app_task.objects.all()[0]
    print("Welcome to revoke = ")
    for ids in app_task:
        #print(ids.task_id)
        app.control.revoke(ids.task_id, terminate=True, signal='SIGKILL')

    print("Done")
    #for schedules in chain.from_iterable(app.control.inspect().scheduled().itervalues()):
    #    print(schedules)
    #chat.control.revokei
    #print(
    #[scheduled["request"]["id"] for scheduled in
    # chain.from_iterable(chat.control.inspect().scheduled()
    #                         .itervalues())])
    
 
