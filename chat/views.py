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
    #killing the running task to avoid duplicacy
    for running_task in Tasks.objects.all():
        if running_task.task_id:
            app.control.revoke(running_task.task_id, terminate=True, signal='SIGUSR1')


    #starting a new task
    result = discord_app_task.delay('chat.bot.run_bot')
    task = Tasks()
    task.task_id = result
    task.save()

    variables = {'message':"Bot Started running",'result':result}
    return render(request, 'running.html', variables)
def abort(request):
    print('Revoke')
    abort_discord_app()

    variables = {'message':"Welcome to Discord Bot page made by Neeraj"}

    return render(request, 'start_bot.html', variables)

def homepage(request):
    variables = {'message':"Welcome to Discord Bot page made by Neeraj"}
    return render(request, 'start_bot.html', variables)

# Create your views here.
