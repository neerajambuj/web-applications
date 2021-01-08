web: gunicorn discord_bot.wsgi
web: python manage.py makemigrations
web: python manage.py migrate
worker: celery -A discord_bot.celery worker -B  -l INFO
