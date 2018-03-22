from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def profile (request, company_id):
    #comapny_dict = getCompany_info(company_id);
    return render(request,'proflePage.html',company_dict)
