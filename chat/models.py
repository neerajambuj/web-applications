from __future__ import unicode_literals

from django.db import models
class Bot(models.Model):
    """
    Model to store the data of the design
    """
    history = models.CharField(max_length=512, verbose_name=u'Query', default = '')
    def __str__(self):
        return '%s' % (self.history)

