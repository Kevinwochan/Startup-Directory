from django.shortcuts import render
from .models import Company
from django.conf.urls.static import static

# display list of companies sorted by date added
def index(request, sortby):
    if isValid_field (sortby) :
        companies = Company.objects.order_by(sortby)
    else : 
        companies = Company.objects.order_by('submission_date')
    return render(request,"index.html",{'companies':companies})

def profile (request, company_id):
#   feitches a dict of a comapny 
    company_dict = get_object_or_404(Company,pk=company_id)

    return render(request,'proflePage.html',{'company_dict':company_dict})

# modify displayed information
def columns(request):

    return

# 
def statistics (request):
    return
# displays a list of comapnies, founders, 
def search (searched_string):
    return


