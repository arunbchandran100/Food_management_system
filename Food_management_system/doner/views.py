from django.shortcuts import render
from .forms import DonateFoodForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DonateFood

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"doner/index.html",{})

@login_required(login_url='login')
def donate_food(request):
    submitted=False
    if request.method== "POST":
        form=DonateFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    # elif request.method== "GET":
    #      form=DonateFoodForm(initial={"user":request.user})
        
    else:    
        form=DonateFoodForm(user_id=request.user) 
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'doner/donatefood.html',{'form':form,'submitted':submitted})


# donation history view
@login_required(login_url='login')
def donation_history(request):
        donation_history=DonateFood.objects.all()
        return render(request,'doner/donation_history.html',{'donation_history':donation_history})

    