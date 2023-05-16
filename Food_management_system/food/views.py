from django.shortcuts import render
from django.http import HttpResponse
from food.models import DonateFood

# Create your views here.

def index(request):
    ctx = {'name':'Food Management System'}
    return render(request, 'food/index.html',ctx)

def vfdetails(request):
    donations = DonateFood.objects.all()
    context = {'donations': donations}
    return render(request, 'food/vfdetails.html', context)

def vohistory(request):
    return render(request, 'food/vohistory.html')

def pmanagement(request):
    return render(request, 'food/pmanagement.html')

def uploadf(request):
    return render(request, 'food/uploadf.html')

def updatef(request):
    return render(request, 'food/updatef.html')

def fddetails(request):
    return render(request, 'food/fddetails.html')

def ohistory(request):
    return render(request, 'food/ohistory.html')

def confirmation(request):
    return render(request, 'food/confirmation.html')
