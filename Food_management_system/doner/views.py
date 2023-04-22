from django.shortcuts import render
from .forms import DonateFoodForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,"doner/index.html",{})


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