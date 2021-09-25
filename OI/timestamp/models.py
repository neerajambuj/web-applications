from django.db import models
#from __future__ import unicode_literals
# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation, ContentType
from django.contrib.auth.models import User, Group
import os
import random
import collections
import string
from string import ascii_uppercase
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.contrib.postgres.fields import JSONField
#from app.models import ContentFileField, get_file_path, JsonFileField

# Create your models here.

class TimeStamp(models.Model):
    """
    Model to store the network information about the network.
    """
    strikePrice = models.IntegerField(verbose_name=u'Change In Open Interest')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    #json_data = JsonFileField(upload_to=get_file_path, blank=True, null=True,verbose_name='All path Data in json file', content_types=['application/json'])

    class Meta:
        verbose_name_plural = 'Topology | Available Networks'
        ordering = ['-created_on']

    def __str__(self):
        return '%s' % self.name




class Call(models.Model):
    """
    Model to store the network information about the network.
    """
    timestamp = models.ForeignKey(
        TimeStamp, related_name='call', verbose_name='Time Stamp', on_delete=models.CASCADE)

    openInterest = models.IntegerField(verbose_name=u'OpenInterest')

    changeInOpenInterest = models.IntegerField(verbose_name=u'Change In Open Interest')

    pChangeInOpenInterest = models.IntegerField(verbose_name=u'Change In Open Interest')

    """
    openInterest = models.IntegerField(
        max_length=255, verbose_name=u'OpenInterest')


    openInterest = models.IntegerField(
        max_length=255, verbose_name=u'OpenInterest')

    description = models.TextField(
        blank=True, null=True, verbose_name=u'Brief Description')
    excel_sheet = ContentFileField(upload_to=get_file_path, blank=True, null=True, verbose_name='Network Data in Excel File', content_types=[
                                   'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'])
 
    user = models.ForeignKey(
        User, related_name='topologies', blank=True, null=True, on_delete=models.CASCADE)
    shared_to = models.ManyToManyField(
        User, related_name='shared_topologies', blank=True,)    
    enable = models.BooleanField(default=True, verbose_name='Enable Network')
    network_type = models.CharField(
        max_length=255, verbose_name='Network Type', default='Linear', choices=NETWORK_TYPES)
    is_imported = models.BooleanField(
        default=False, verbose_name='Imported Network ?')
    is_green_field = models.BooleanField(
        default=True, verbose_name='Green Field Network ?')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    json_data = JsonFileField(upload_to=get_file_path, blank=True, null=True,verbose_name='All path Data in json file', content_types=['application/json'])

    class Meta:
        verbose_name_plural = 'Topology | Available Networks'
        ordering = ['-created_on']
    """


    def __str__(self):
        return '%s' % self.name

class Put(models.Model):
    """
    Model to store the network information about the network.
    """
    timestamp = models.ForeignKey(
        TimeStamp, related_name='put', verbose_name='Time Stamp', on_delete=models.CASCADE)

    openInterest = models.IntegerField( verbose_name=u'OpenInterest')

    changeInOpenInterest = models.IntegerField(verbose_name=u'Change In Open Interest')

    pChangeInOpenInterest = models.IntegerField(verbose_name=u'Change In Open Interest')

    def __str__(self):
        return '%s' % self.name

