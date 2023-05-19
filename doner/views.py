from django.shortcuts import render
from .forms import DonateFoodForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DonateFoodModel
from django.views.generic import TemplateView

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"doner/index.html",{})

class DonateFoodView(TemplateView):
    form_class=DonateFoodForm
    model=DonateFoodModel
    template_name = "doner/donatefood.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class(initial={"user":request.user})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, self.template_name, self.context)


class DonationHistoryView(TemplateView):
    def get(self, request, *args, **kwargs):
        donation_history=DonateFoodModel.objects.all().filter(user=request.user)
        context={}
        context["donation_history"]=donation_history
        return render(request,"doner/donation_history.html",context)