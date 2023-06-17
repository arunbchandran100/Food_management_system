from django.shortcuts import render, redirect
from .forms import RequestDonationForm
from .models import RequestDonation
from doner.models import DonateFoodModel
from website.models import Profile
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User#, UserChangeForm
#from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .helpers import send_forget_password_mail
#import passlib.pwd  
from website.models import Profile
from django.urls import reverse

from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def index1(request):
    return render(request,"food/index1.html",{})


@login_required(login_url='login')
def d_view_profile(request):
  if request.method == 'POST':
    return redirect(reverse('food:d_view_profile'))

  return render(request, 'food/d_view_profile.html')


@login_required
def d_edit_profile(request):
    if request.method == 'POST':
        # Get the data that the user submitted from the form.
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        user_type = request.POST.get('user_type')

        # Check if the new email is already in use by another user.
        if User.objects.exclude(id=request.user.id).filter(email=email).exists():
            error_message = f"The email id {email} is already used by another user. Please choose another."
            messages.add_message(request, messages.ERROR, error_message)

        # Check if the new mobile number is already in use by another user.
        if Profile.objects.exclude(user=request.user).filter(mobile=mobile).exists():
            messages.add_message(request, messages.ERROR, f"The mobile number '{mobile}' is already in use by another user. Please choose another.")

        # If there are any error messages, redirect to the edit profile page.
        if messages.get_messages(request):
            return redirect('d_edit_profile')
        
        # Update the user's profile details in the database.
        my_user = request.user
        my_user.first_name = first_name
        my_user.last_name = last_name
        my_user.email = email
        my_user.username=email
        my_user.save()

        profile = Profile.objects.get(user=my_user)
        profile.mobile = mobile
        profile.user_type = user_type
        profile.save()

        # Redirect the user to the profile page.
        return redirect('d_view_profile')

    else:
        # If the request method is not POST, render the edit profile page.
        return render(request, 'food/d_edit_profile.html')


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
