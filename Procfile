web: gunicorn discord_bot.wsgi
worker: celery worker -A tasks.app -l INFO
