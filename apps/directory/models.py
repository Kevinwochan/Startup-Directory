from django.db import models

class Company (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    founded_date = models.DateField()
    founders = models.CharField(max_length=200)
    stage = models.CharField(max_length=200)
    submission_date = models.DateTimeField()
    industries = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    logo = models.ImageField(upload_to='logos')
