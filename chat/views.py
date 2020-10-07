from django.shortcuts import render
from django.http import HttpResponse
from chat.bot import run_bot
def Run(request):
    run_bot()
    return HttpResponse("Bot Started Running")
# Create your views here.
