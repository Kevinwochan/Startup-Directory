from django.shortcuts import render, get_object_or_404
from .models import Company
from django.conf.urls.static import static
from django.forms.models import model_to_dict

# display list of companies sorted by date added
def index (request, sortby):
    if isValid_field (sortby):
        companies = Company.objects.order_by(sortby)
    else:
        companies = Company.objects.order_by('submission_date')
    return render(request,"index.html",{'companies':companies})

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

def isValid_field ( field ):

    try:
        Company._meta.get_field(field)
    except: 
        return 0
    return 1
