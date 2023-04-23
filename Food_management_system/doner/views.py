from django.shortcuts import render
from .forms import DonateFoodForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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
        
    else:    
        form=DonateFoodForm 
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'doner/donatefood.html',{'form':form,'submitted':submitted})