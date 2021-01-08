from django.conf.urls import url, include

from scheduler.views import  kill_a_scheduled_task

urlpatterns = [
    url(r'^kill/(?P<id>\d+)/$', kill_a_scheduled_task),
]
