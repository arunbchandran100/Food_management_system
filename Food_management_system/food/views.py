from django.shortcuts import render, redirect
from .forms import RequestDonationForm
from .models import RequestDonation
from doner.models import DonateFood

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
    return render(request,"food/index.html",{})

@login_required(login_url='login')
def request_donation(request):
    submitted = False
    if request.method == "POST":
        form = RequestDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RequestDonationForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'food/request_donation.html', {'form': form, 'submitted': submitted})

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
