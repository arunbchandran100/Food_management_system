from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    ctx = {'name':'Food Management System'}
    return render(request, 'food/index.html',ctx)

def vfdetails(request):
    return render(request, 'food/vfdetails.html')

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
