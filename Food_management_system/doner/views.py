from django.shortcuts import render
from .forms import DonateFoodForm,FeedbackForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DonateFoodModel,FeedbackModel
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from datetime import date
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"doner/index.html",{})


@method_decorator(login_required,name='dispatch')
class DonateFoodView(TemplateView):
    form_class=DonateFoodForm
    model=DonateFoodModel
    template_name = "doner/donatefood.html"
    context={}
    def get(self, request, *args, **kwargs):
        today = timezone.localdate()
        form=self.form_class(initial={"user":request.user,"date":today})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, self.template_name, self.context)

class DonationEditView(TemplateView):
    model=DonateFoodModel
    form_class=DonateFoodForm
    template_name="doner/donatefood.html"
    context={}
    def get(self,request,*args,**kwargs):
        edit=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(instance=edit)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        edit=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect("donation-history")
        else:
            return render(request,self.template_name,self.context)
        
class DonationDeleteView(TemplateView):
    model=DonateFoodModel
    def get(self,request,*args,**kwargs):
        item=self.model.objects.get(id=kwargs["pk"])
        item.delete()
        return redirect('donation-history')

@method_decorator(login_required,name='dispatch')
class DonationHistoryView(TemplateView):
    def get(self, request, *args, **kwargs):
        donation_history=DonateFoodModel.objects.all().filter(user=request.user)
        context={}
        context["donation_history"]=donation_history
        return render(request,"doner/donation_history.html",context)
    
@method_decorator(login_required,name='dispatch')
class FeedbackView(TemplateView):
    model=FeedbackModel
    form_class=FeedbackForm
    context={}
    template_name = "doner/feedback.html"
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={"user": request.user})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, self.template_name, self.context)
    
@method_decorator(staff_member_required,name='dispatch')
class FeedbacklistView(TemplateView):
    def get(self, request, *args, **kwargs):
        lists=FeedbackModel.objects.all()
        context={}
        context["lists"] = lists
        return render(request,"doner/feedbacklist.html",context)
    
