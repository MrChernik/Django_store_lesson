from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {
        'title': 'Grab Grib'
    }
    return render(request,'main/index.html', data)

def market(request):
    data ={
        'title': 'GG: Товарный ряд'
    }
    return render(request,'main/marketplace.html', data)
def about(request):
    data = {
        'title': 'О проекте GG'
    }
    return render(request,'main/about.html', data)
