from __future__ import unicode_literals
from django.db import models  # Default django models
from django.contrib.auth.models import User  # User Model
from django.utils import timezone
from datetime import datetime, timedelta, date
import os
import random
import collections

from django.db import models
class Tasks(models.Model):
    """
    Model to store the task details and track the same with respect to particular user
    """
    task_id = models.SlugField(editable=False, null=True, unique=True)



# Create your models here.
