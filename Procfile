web: gunicorn discord_bot.wsgi
worker: celery worker -A discord.celery worker -B  -loglevel=info
