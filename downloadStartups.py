from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from directory.models import Company
import sqlite3
from datetime import datetime
# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
SPREADSHEET_ID = '1xAodlUoUTu0NJYoLBdFRWSPnRNeBeoVpuP_2neOdfOA'
RANGE_NAME = 'Sanitised Data!A:K'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    # extract the spreadsheet headers, fields[0] = logo, fields[1] = name
    fields = values[0]
    print(fields)
    for row in values[1:]:
        if Company.objects.filter(name=row[1]).exists():
            print ('==== updating ' + row[1] + ' ====')
            company = Company.objects.get(name=row[1])
        else:
            company=Company()
            print ('==== saving ' + row[1] + ' ====')
        for field in range(0,8):
            if row[field] == '':
                default_value = Company._meta.get_field(fields[field]).get_default()
                setattr(company, fields[field], default_value)
            else:
                if ( fields[field] == 'logo' ):
                    os.path
                    setattr(company, fields[field], row[field])
                else:
                    setattr(company, fields[field], row[field])
            print('    ' + fields[field] + ': ' + row[field])
        company.submission_date=datetime.now()
        company.save()
        print ( '==================' )
