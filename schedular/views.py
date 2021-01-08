from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
def kill_a_scheduled_task(request, id):
    """
    Function to kill a task
    """
    try:
        task = Task.objects.get(id=id)
        task.state = 'TERMINATED'
        task.task_progress = 100
        task.is_completed = True
        task.save()
        app.control.revoke(task.celery_task_id, terminate=True, signal='SIGKILL')
    except:
        print(sys.exc_info())
        aptlogger.debug(sys.exc_info())
    return HttpResponseRedirect("/tasks/completed/")
# Create your views here.
