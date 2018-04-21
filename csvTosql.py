import os
from directory.models import Company
import sqlite3
import csv
from datetime import datetime
import re
os.environ['DJANGO_SETTINGS_MODULE'] = "startupdirectory.settings.development"
PROJECT_DIR = os.getcwd()
csv_filepath = os.path.join( PROJECT_DIR,'startups.csv')
with open(csv_filepath,'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if Company.objects.filter(name=row['name']).exists():
            company = Company.objects.get(name=row['name'])
            print ('==== updating ' + row['name'] + ' ====')
            for field in iter(row):
                if row[field] == '':
                    default_value = Company._meta.get_field(field).get_default()
                    setattr(company, field, default_value)
                else:
                    setattr(company, field, row[field])
                print('    ' + field + ': ' + row[field])
            company.save()
            print ( '===== update sucessful =====' )
        else:
            company=Company()
            print ('==== saving ' + row['name'] + ' ====')
            for field in iter(row):
                if row[field] == '':
                    default_value = Company._meta.get_field(field).get_default()
                    setattr(company, field, default_value)
                else:
                        setattr(company, field, row[field])
                print('    ' + field + ': ' + row[field])
            company.submission_date=datetime.now()
            company.save()
            print ( '===== save succesful =====' )
