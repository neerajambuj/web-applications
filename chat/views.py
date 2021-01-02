from django.shortcuts import render
from django.http import HttpResponse
from chat.bot import run_bot
from chat.models import Bot
#from schedular.tasks import apt_app_task
from django.views.generic.edit import FormView
from chat.forms import BOT
from chat.tasks import run_bot_task
from schedular.tasks import discord_app_task
from abort_discord import abort_discord_app
class StartBot(FormView):
    template_name = 'start_bot.html'
    form_class = BOT
    def form_valid(self, form):
        return HttpResponse("Bot Started Running")

def launch(request):
    #result = run_bot_task.delay()
    #print(type(result),result)
    print("Successfully Launched")
    #result = run_bot_task.delay()#apply_async(countdown=1)
    discord_app_task.delay('chat.bot.run_bot')
    variables = {'message':"Bot Started running"}#'result':result}
    #return render(request, 'running.html', variables)
    return HttpResponse("Bot Started Running")   
'''def abort(request):
    print('Revoke')
    #print(result)
    #result.revoke()
    abort_discord_app()
    template_name =  'start_bot.html'
    form_class = BOT
    #run_bot_task.delay()
    #run_bot_task.apply_async(countdown=10)
    variables = {'message':"Bot Stooped running"}
    return render(request, 'start_bot.html', variables)
'''
def homepage(request):
    #run_bot()
    #apt_app_task.delay('chat.bot.run_bot')
    variables = {'message':"Welcome to Discord Bot page made by Neeraj"}
    return render(request, 'start_bot.html', variables)

# Create your views here.
