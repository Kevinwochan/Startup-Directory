#!/usr/bin/env python
import sys, os

# define settings for django
os.environ("DJANGO_SETTINGS_MODULE", "startupdirectory.settings.development")


from apps.directory.models import Company

# get current working directory
PROJECT_DIR = os.getcwd()
# get csv file 
csv_filepath = os.path.join( PROJECT_DIR,'startups.csv')

import sqlite3
sql = sqlite3.connect('development.db')
cur = sql.cursor()

import csv  
fd = open(csv_filepath,'r')
next(f, None) # skip the header row
dataReader = csv.reader(fd, delimiter=',', quotechar='"')

from datetime import datetime
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
    sql.commit()

	
fd.close()
sql.close()


