from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Sender(models.Model):
    ip_address = models.CharField(max_length=40)
    last_sent = models.CharField(max_length=40, default=datetime.datetime.now().strftime("%Y-%m-%d"))
    sent_count = models.IntegerField()
