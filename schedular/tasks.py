# -*- coding: utf-8 -*-
"""
This file has the functions to run the tasks by the scheduler
"""
from celery import task  # Import task from celery
#from scheduler.models import Task
import sys
import traceback
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.module_loading import import_string
import random
import string


@task(name="discord_app_task")
def discord_app_task(func):#, kwargs):
    """
    Default function to handle all asynchronous tasks of the software. It will take function name as argument and will call the respective function along with the passed arguments.
    Args:
        func : Function Name to call
        kwargs : All the arguments
    """
    print("Discord Bot Process is called")
    try:
        '''
        #print(apt_app_task.request.id)
        user = User.objects.get(id=int(kwargs['userid']))
        args = kwargs  # Store arguments
        # Create a task to track the complete process
        task = Task()
        task.user = user
        task.name = kwargs['name']
        if func == "topology.parsers.save_parsed_excel_file":
            task.success_msg = kwargs['network']
        task.start_time = datetime.now()
        task.task_function = func
        task.task_arguments = kwargs
        task.is_started = True
        task.state = 'IN-PROGRESS'
        task.task_id = str(''.join(random.choice(
            string.ascii_letters + string.digits) for i in range(32)))
        task.celery_task_id = apt_app_task.request.id
        task.save()
        aptlogger.debug("Task %s is created" % task.name)
        # Add task id to arguments
        args['taskid'] = task.id
        # Call the function
        '''
        function = import_string(func)  # Import the function
        #function(args)
        function()
    except:  # If something went wrong
        print(sys.exc_info())
        print(traceback.print_exception(*sys.exc_info()))
        print(traceback.format_exc())
    return None  # It will not return anything
