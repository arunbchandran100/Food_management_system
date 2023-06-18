from django.shortcuts import render, redirect
from .forms import RequestDonationForm,OrderForm
from .models import RequestDonation, OrdersModel
from doner.models import DonateFoodModel
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index1(request):
    return render(request, "food/index1.html", {})


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
