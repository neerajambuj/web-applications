web: gunicorn discord_bot.wsgi
worker: celery -A discord_bot.celery worker -B  -l INFO
