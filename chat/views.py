from django.shortcuts import render


from celery import Celery
from itertools import chain
from discord_bot.celery import app
from billiard.exceptions import Terminated




from django.http import HttpResponse
from chat.bot import run_bot
from chat.models import Bot
#from schedular.tasks import apt_app_task
from django.views.generic.edit import FormView
from chat.forms import BOT
#from chat.tasks import run_bot_task
from chat.abort_discord import abort_discord_app
from schedular.tasks import discord_app_task
from schedular.models import Tasks
class StartBot(FormView):
    template_name = 'start_bot.html'
    form_class = BOT
    def form_valid(self, form):
        return HttpResponse("Bot Started Running")

def launch(request):
    #result = run_bot_task.delay()
    #print(type(result),result)
    #print("Successfully Launched")
    #result = run_bot_task.delay()#apply_async(countdown=1)
    '''for running_task in Tasks.objects.all():
        if running_task.task_id:
            #variables = {'message':"Bot Started running"}
            #return render(request, 'running.html', variables)
            app.control.revoke(running_task.task_id, terminate=True, signal='SIGUSR1')
    '''
    result = discord_app_task.delay('chat.bot.run_bot')
    task = Tasks()
    task.task_id = result
    task.save()
    #print(result)
    variables = {'message':"Bot Started running",'result':result}
    return render(request, 'running.html', variables)
    #return HttpResponse("Bot Started Running")   
def abort(request):
    print('Revoke')
    #print(result)
    #result.revoke()
    #discord_app_task.delay('chat.abort_discord.abort_discord_app')
    #template_name =  'start_bot.html'
    #form_class = BOT
    #run_bot_task.delay()
    #run_bot_task.apply_async(countdown=10)
    variables = {'message':"Welcome to Discord Bot page made by Neeraj"}

    return render(request, 'start_bot.html', variables)

def homepage(request):
    #run_bot()
    #apt_app_task.delay('chat.bot.run_bot')
    variables = {'message':"Welcome to Discord Bot page made by Neeraj"}
    return render(request, 'start_bot.html', variables)

# Create your views here.
