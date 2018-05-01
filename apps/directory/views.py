from django.shortcuts import render, get_object_or_404
from .models import Company
from django.conf.urls.static import static
from django.forms.models import model_to_dict
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# default starting page (empty url request)
def home (request):
    companies = Company.objects.all().order_by('submission_date')

    paginator = Paginator(companies,15)
    page = request.GET.get('page')
    companies = paginator.get_page(page)
    options = fields_dict()

    return render(request,"index.html",{'companies':companies})


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
    options = fields_dict()

    return render (request,"index.html",{'companies':companies,'lambdas':lambdas})


#   fetches a company based on id
def profile (request, company_id):
    company_obj = get_object_or_404(Company,pk=company_id)
    company = model_to_dict(company_obj)
    company['founders'] = company['founders'].split(',')

    return render (request,'profile.html',{'company':company})

def field_filter (request, field, filter):
    companies_obj = Company.objects.filter(**{field:filter})
    options = fields_dict()

    return render (request,'index.html',{'companies':companies_obj,'options':options})


def search (searched_string):
    return


# returns an immutable list of all options for a field
def options_list (field):
    options = Company.objects.__meta.get(field).choices

    return options


# returns a dictionary of field options for a field
def fields_dict ():
    for field in Company.objects.__meta.get_fields():
        dict[field] = options_list (field)

    return dict
