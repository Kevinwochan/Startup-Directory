from django.db import models

class Company (models.Model):
    company_name = models.CharField(max_length=200)
    company_description = models.CharField(max_length=200)
    submission_date = models.DateTimeField('submission date')
    industries = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)

class Question (models.Model):
   question_text = models.CharField(max_length=200)
   def __str__(self):
       return self.question_text
    
class Answer (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
       return self.answer_text
    
