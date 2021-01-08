web: gunicorn discord_bot.wsgi
worker: celery worker -A discord_bot.celery worker -B  -loglevel=info
