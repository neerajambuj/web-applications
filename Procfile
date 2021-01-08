web: gunicorn discord_bot.wsgi
web: python3 manage.py makemigrations
web: python3 manage.py migrate
worker: celery -A discord_bot.celery worker -B  -l INFO
