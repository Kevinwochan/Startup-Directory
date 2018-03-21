"""Base models"""
from django.db import models

class company (models.Model):
    compane_name = models.CharField(max_length=200)
    company_description = models.CharField(max_length=1000)

