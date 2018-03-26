from django.db import models

class Company (models.Model):
    company_name = models.CharField(max_length=200)
    company_description = models.CharField(max_length=200)
    submission_date = models.DateTimeField('submission date')
    industries = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)
   
