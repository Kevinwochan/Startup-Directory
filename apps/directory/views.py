from django import forms
from django.shortcuts import render, get_object_or_404
from .models import Company
from django.conf.urls.static import static
from django.forms.models import model_to_dict
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home (request):
    companies = Company.objects.all().order_by('submission_date')

    paginator = Paginator(companies,15)
    page = request.GET.get('page')
    companies = paginator.get_page(page)
    options = filter_options()

    return render(request,"index.html",{'companies':companies,'options':options})


# display list of companies sorted by date added
def index (request, sorting_string, page):
    companies = Company.objects.all()
    if sorting_string != '':
        # extracts multiple sort lambdas
        lambdas = re.findall(r'[-a-z_]+', sorting_string)
        for sortby in lambdas:
            if lambdas == 'funding':
                companies = companies.order_by('funding').order_by('funding_unit')
            else:
                companies = companies.order_by(sortby)
    else:
        lambdas = ''
        companies = Company.objects.order_by('submission_date')

    paginator = Paginator(companies,15)
    page = request.GET.get('page')
    companies = paginator.get_page(page)
    options = filter_options()

    return render(request,"index.html",{'companies':companies,'lambdas':lambdas,'options':options})


#   fetches a company based on id
def profile (request, company_id):
    company_obj = get_object_or_404(Company,pk=company_id)
    company = model_to_dict(company_obj)
    company['founders'] = company['founders'].split(', ').strip(', ')

    return render (request,'profile.html',{'company':company})

# display category requests
def show_category (request, field, category):
   companies_obj = Company.objects.filter(**{field:category})
   options = filter_options()

   return render (request,'index.html',{'companies':companies_obj,'options':options})

# display companies matching filters
def filter (request, filter_string):
    industry = request.GET.get('industry')
    stage = request.GET.get('stage')
    founded_year = request.GET.get('founded_year')
    companies_obj = Company.objects.filter('industry',industry)
    options = filter_options()

    return render (request,'index.html',{'companies':companies_obj,'options':options})



# intialise a dict of field options
def filter_options ():
    options = {}
    for field in ['stage','year_founded','industries']:
        if Company._meta.get_field(field).choices:
            options[field] = []
            for choice in Company._meta.get_field(field).choices:
                options[field].append(choice[0])
    return options

def search (searched_string):
    return

