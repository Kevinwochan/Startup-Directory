from django.shortcuts import render, get_object_or_404
from .models import Company
from django.conf.urls.static import static
from django.forms.models import model_to_dict
import re

# display list of companies sorted by date added
def index (request, sorting_string):
    print( 'sort string is : '+ sorting_string)
    companies = Company.objects.all()
    if sorting_string != '':
        # extracts multiple sort lambdas
        lambdas = re.findall(r'[-a-z_]+', sorting_string)
        print( lambdas)
        for sortby in lambdas:
            print("sortby is " + sortby)
            if lambdas == 'funding':
                companies = companies.order_by('funding').order_by('funding_unit')
            else:
                companies = companies.order_by(sortby)
    else:
        lambdas = ''
        companies = Company.objects.order_by('submission_date')
    return render(request,"index.html",{'companies':companies,'lambdas':lambdas})

def profile (request, company_id):
#   fetches a company based on id
    company_obj = get_object_or_404(Company,pk=company_id)
    company = model_to_dict(company_obj)
    company['founders'] = company['founders'].split(',')
    return render(request,'profile.html',{'company':company})


# modify displayed information
def columns(request):
    return


def statistics (request):
    return
# displays a list of comapnies, founders, 
def search (searched_string):
    return

# checks sorting string is valid
def isValid_sortingString ( sorting_string):
    for field in re.findall(r'-*?[a-z_]+&*?', sorting_string):
        if not isValid_field (field):
            return 0
    return 1

# checks field give is valid 
def isValid_field ( field ):
    try:
        Company._meta.get_field(field)
    except: 
        return 0
    return 1
