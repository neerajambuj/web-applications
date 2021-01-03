from celery import Celery
#from chat.bot import run_bot
app = Celery()
app.config_from_object("celery_settings")



@app.task
def task():
    #run_bot.delay()
    print("All good")
