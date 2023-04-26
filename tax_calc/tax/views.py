from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is a site to calculate tax</h1>')

def taxcalc(request,var):
    var = var+ var*0.15
    return HttpResponse(f'The total is,{var}')

def taxrate(request):
    tax_rate=str('15%')
    context = {'tax_rate': tax_rate}
    return render(request , "tax/taxrate.html",context)

    
    

# Create your views here.
