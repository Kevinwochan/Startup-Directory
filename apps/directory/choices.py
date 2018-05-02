from django.utils import timezone
from datetime import date, datetime

# creates dyamic set of choices for founded date
YEAR_CHOICES = [] 
for r in range(2010, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
YEAR_CHOICES.append(('',''))

# creates a set of choices for funding units, k for 1 000, m for 1,000,000 etc
UNIT_LIST = ('','Undisclosed','K','M','B')
UNIT_CHOICES = []
for r in UNIT_LIST:
    UNIT_CHOICES.append((r,r))

#FUNDING_LIST = ('Ideation','MVP','Seed', 'SeriesA', 'SeriesB', 'SeriesC', 'SeriesD', 'SeriesE', 'SeriesF', 'SeriesG', 'SeriesH', 'SeriesI', 'SeriesJ', 'Venture-SeriesUnknown', 'Angel', 'PrivateEquity', 'DebtFinancing', 'ConvertibleNote', 'Grant', 'CorporateRound', 'EquityCrowdfunding', 'ProductCrowdfunding', 'SecondaryMarket', 'Post-IPOEquity', 'Post-IPODebt', 'Post-IPOSecondary', 'Non-equityAssistance', 'InitialCoinOffering', 'Undisclosed', )
FUNDING_LIST = ('','Undisclosed','Pre-product','Pre-launch','Launch','Revenue')
FUNDING_CHOICES = []
for r in FUNDING_LIST:
    FUNDING_CHOICES.append((r,r))


INDUSTRY_LIST = ('',"Advertising","Agriculture","Apps","Artificial Intelligence","Biotechnology",
        "Consumer Electronics","E-Commerce","Education","FinTech","Food and Beverage",
        "Health Care","Health Diagnostics","Human Resources","Industrial","Internet of Things",
        "Marketplace","Mobile Apps","Quality Assurance","Retail","Space","Sports","Tourism",
        "Transportation")
INDUSTRY_CHOICES=[]
for r in INDUSTRY_LIST:
    INDUSTRY_CHOICES.append((r,r))


