from django import forms
from django.shortcuts import render, get_object_or_404
from .models import Company
from .forms import filterForm
from django.conf.urls.static import static
from django.forms.models import model_to_dict
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def home (request):
    companies = Company.objects.all().order_by('submission_date')

    paginator = Paginator(companies,15)
    page = request.GET.get('page')
    companies = paginator.get_page(page)
    form = filterForm()

    return render(request,"index.html",{'companies':companies,'filter_form':filterForm})


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

    return render(request,"index.html",{'companies':companies,'lambdas':lambdas,'filter_form':filterForm})


#   fetches a company based on id
def profile (request, company_id):
    company = get_object_or_404(Company,pk=company_id)

    return render (request,'profile.html',{'company':company})

# display category requests
def show_category (request, field, category):
    category=category.replace("%20",' ')
    companies_obj = Company.objects.filter(**{field:category})

    return render (request,'index.html',{'companies':companies_obj,'filter_form':filterForm})

# display companies matching filters
def filter (request):

    industry_filter = request.GET.get('industry')
    stage_filter = request.GET.get('stage')
    year_filter = request.GET.get('year')

    companies_obj = Company.objects.all()
    if industry_filter:
        companies_obj = companies_obj.filter(industries=industry_filter)
    if stage_filter:
        companies_obj = companies_obj.filter(stage=stage_filter)
    if year_filter:
        companies_obj = companies_obj.filter(year_founded=year_filter)

    query = request.GET.get("q")
    if query:
        companies_obj = companies_obj.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(industries__icontains=query) |
        Q(stage__icontains=query)
        ).distinct()

    return render (request,'index.html',{'companies':companies_obj,'filter_form':filterForm})



def search (searched_string):
    return
