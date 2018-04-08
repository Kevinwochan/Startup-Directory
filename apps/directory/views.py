from django.shortcuts import render
from .models import Company
from django.conf.urls.static import static

# Create your views here.
def index(request):
    companies = Company.objects.order_by('submission_date')
    return render(request,"index.html",{'companies':companies})

def profile (request, company_id):
    #comapny_dict = getCompany_info(company_id)A

#   feitches a dict of a comapny 
    company_dict = get_object_or_404(Company,pk=company_id)
    
    return render(request,'proflePage.html',{'company_dict':company_dict})
