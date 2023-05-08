from django.shortcuts import render
from .forms import DonateFoodForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DonateFood

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"distributor/index.html",{})

@login_required(login_url='login')
def donate_food(request):
    submitted=False
    if request.method== "POST":
        form=DonateFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        
    else:    
        form=DonateFoodForm 
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'distributor/donatefood.html',{'form':form,'submitted':submitted})


# donation history view
def donation_history(request):
        donation_history=DonateFood.objects.all()
        return render(request,'distributor/donation_history.html',{'donation_history':donation_history})

    