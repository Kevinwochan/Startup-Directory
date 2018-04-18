from django.db import models

class Company (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    founded_date = models.CharField(max_length=200)
    stage = models.CharField(max_length=200)
    submission_date = models.DateTimeField('submission date')
    industries = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
