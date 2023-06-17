from django.shortcuts import render, redirect
from .forms import RequestDonationForm
from .models import RequestDonation
from doner.models import DonateFoodModel

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def index1(request):
    return render(request,"food/index1.html",{})

@login_required(login_url='login')
def request_donation(request):
    submitted = False
    if request.method == "POST":
        form = RequestDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RequestDonationForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'food/request_donation.html', {'form': form, 'submitted': submitted})

def vfdetails(request):
    donations = DonateFoodModel.objects.all()
    context = {'donations': donations}
    return render(request, 'food/vfdetails.html', context)

def vohistory(request):
    return render(request, 'food/vohistory.html')

def pmanagement(request):
    return render(request, 'food/pmanagement.html')

def order(request, donation_id):
    # Logic to process the order for the given donation_id
    donation = DonateFoodModel.objects.get(id=donation_id)
    # Additional processing code
    context = {
        'donation': donation
    }
    return render(request, 'food/order.html', context)

def viewreq(request):
    requested_donations = RequestDonation.objects.all()
    context = {'requested_donations': requested_donations}
    return render(request, 'food/viewreq.html', context)

def fddetails(request):
    return render(request, 'food/fddetails.html')

def ohistory(request):
    return render(request, 'food/ohistory.html')

def confirmation(request):
    return render(request, 'food/confirmation.html')
