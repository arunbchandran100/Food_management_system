from django import forms
from .models import DonateFoodModel,FeedbackModel
from django.forms import ModelForm

class DonateFoodForm(ModelForm):
    choice1=[
       ("Hotel","Hotel"),
       ("Catering","catering"),
       ("Hostels","Hostels"),
       ("Normal user","Normal user")
    ]
    choice2=[
        ("biriyani","biriyani"),
        ("rice","rice"),
        ("porota curry","porota curry"),
        ("puttu curry","puttu curry")
    ]
    choice3=[
        ("veg","veg"),
        ("Nonveg","Nonveg"),
        ("Both","Both")
    ]
    donor_type = forms.ChoiceField(choices=choice1, required=True,widget=forms.Select(attrs={'class': 'input','id':'dof-fld'}) )
    food_type = forms.ChoiceField(choices=choice3, required=True,widget=forms.Select(attrs={'class': 'input','id':'dof-fld'}) )
    food = forms.ChoiceField(choices=choice2, required=True,widget=forms.Select(attrs={'class': 'input','id':'dof-fld'}) )
    donor_discription= forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'input','id':'dof-fld'}))
    food_discription= forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'input','id':'dof-fld'}))

    class Meta:
        model=DonateFoodModel
        fields="__all__"
        widgets = {

            'user': forms.TextInput(attrs={'class': 'input','id':'dof-fld'}),
            'location': forms.TextInput(attrs={'class': 'input','id':'dof-fld'}),
            'date': forms.TextInput(attrs={'class': 'input','id':'dof-fld'}),
            'counts': forms.TextInput(attrs={'class': 'input','id':'dof-fld'}),
            'Expire_date': forms.TextInput(attrs={'class': 'input','id':'dof-fld'})



        }

class FeedbackForm(ModelForm):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 8,'class':'input'}))
    class Meta:
        model=FeedbackModel
        fields=['user','feedback']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'input'}),
        }
