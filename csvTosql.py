from dateime import datetime
import sys, os
from startupdirectory.directory.models import Company
import csv

# get current working directory
PROJECT_DIR = os.getcwd()
# get csv file 
csv_filepath = os.path.join( PROJECT_DIR,'startups.csv')

os.environ['DJANGO_SETTINGS_MODULE'] = 'startupdirectory.settings'


dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    company=Company()
    company.name=row[0]
    company.founded_year=row[1]
    company.website=row[2]
    company.industries=row[3]
    company.description=row[4]
    company.stage=row[5]
    company.submission_date=datetime.datetime.now()

    company.save()
 
