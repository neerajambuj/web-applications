from django.apps import apps
from django.contrib import admin

myapp = apps.get_app_config('schedular')
for model in myapp.get_models():
    admin.site.register(model)

# Register your models here.
