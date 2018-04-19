from django.utils import timezone
from datetime import date
from django.db import models

class Company (models.Model):
    name = models.CharField(max_length=200, default='undefined')
    description = models.CharField(max_length=200, default='undefined')
    founded_date = models.DateField(default=date.today)
    founders = models.CharField(max_length=200,default="undefined")
    stage = models.CharField(max_length=200,default="undefined")
    submission_date = models.DateTimeField(default=timezone.now)
    industries = models.CharField(max_length=200,default="undefined")
    website = models.URLField(max_length=200,default="undefined")
    email = models.EmailField(max_length=200,default="undefined")
    logo = models.ImageField(upload_to='logos',default="/logo/undefined.png")
