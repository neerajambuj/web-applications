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
def discord_app_task(func):
    """
    Default function to handle all asynchronous tasks of the software. It will take function name as argument and will call the respective function .
    Args:
        func : Function Name to call
    """
    print("Discord Bot Process is called")
    try:
        function = import_string(func)  # Import the function
        function()
    except:  # If something went wrong
        print(sys.exc_info())
        print(traceback.print_exception(*sys.exc_info()))
        print(traceback.format_exc())
    return None  # It will not return anything
