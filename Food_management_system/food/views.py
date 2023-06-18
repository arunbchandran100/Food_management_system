from django.shortcuts import render, redirect
from .forms import RequestDonationForm,OrderForm
from .models import RequestDonation, OrdersModel
from doner.models import DonateFoodModel
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from website.models import Profile
from django.contrib import messages

from website.models import Profile
from django.urls import reverse

from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.models import User


@login_required(login_url='login')
def index1(request):
    return render(request, "food/index1.html", {})


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



@method_decorator(login_required, name='dispatch')
class RequestDonationView(TemplateView):
    form_class = RequestDonationForm
    model = RequestDonation
    template_name = "food/request_donation.html"
    context = {}

    def get(self, request, *args, **kwargs):
        today = timezone.localdate()
        form = self.form_class(initial={"user": request.user, "request_date": today})
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("food:index1")
        return render(request, self.template_name, self.context)


class RequestEditView(TemplateView):
    model = RequestDonation
    form_class = RequestDonationForm
    template_name = "food/request_donation.html"
    context = {}

    def get(self, request, *args, **kwargs):
        edit = self.model.objects.get(id=kwargs["pk"])
        form = self.form_class(instance=edit)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        edit = self.model.objects.get(id=kwargs["pk"])
        form = self.form_class(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect("food:viewreq")
        else:
            return render(request, self.template_name, self.context)


class RequestDeleteView(TemplateView):
    model = RequestDonation

    def get(self, request, *args, **kwargs):
        item = self.model.objects.get(id=kwargs["pk"])
        item.delete()
        return redirect("food:viewreq")


def vfdetails(request):
    donations = DonateFoodModel.objects.all()
    context = {'donations': donations}
    return render(request, 'food/vfdetails.html', context)


def vohistory(request):
    orders = OrdersModel.objects.filter(user=request.user)
    context = {
        'orders': orders
    }
    return render(request, 'food/vohistory.html', context)

def pmanagement(request):
    return render(request, 'food/pmanagement.html')


from .forms import OrderForm

def order(request, donation_id):
    donation = DonateFoodModel.objects.get(id=donation_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.donor = donation.user
            order.donor_type = donation.donor_type
            order.donor_discription = donation.donor_discription
            order.food_type = donation.food_type
            order.food = donation.food
            order.food_discription = donation.food_discription
            order.date = donation.date
            order.location = donation.location
            order.user = request.user
            order.save()
            # Additional processing code for the created order
            return redirect("food:confirmation")
    else:
        form = OrderForm()
    context = {
        'form': form,
        'donation': donation
    }
    return render(request, 'food/order.html', context)



def viewreq(request):
    requested_donations = RequestDonation.objects.filter(user=request.user)
    context = {'requested_donations': requested_donations}
    return render(request, 'food/viewreq.html', context)


def fddetails(request):
    return render(request, 'food/fddetails.html')


def ohistory(request):
    return render(request, 'food/ohistory.html')


def confirmation(request):
    return render(request, 'food/confirmation.html')
