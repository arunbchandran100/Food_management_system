from django import forms
from django.forms import ModelForm
from .models import DonateFood
from django.contrib.auth.models import User

class DonateFoodForm(ModelForm):
    class Meta:
        model=DonateFood
        fields="__all__"
        Description= forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'input food-donate-form'}))
        labels= {

            'user': '',
            'food_type': '',
            'discription': '',
            'supply_date': '',
            'pickup_location': '',
            'pickup_deadline': '',
            'contact_information':'',
        }
        widgets = {

            'user': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'user name',}),
            'food_type': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'type of food'}),
            'discription': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'food description'}),
            'supply_date': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'supply date (YYYY-MM-DD)'}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'pickup location'}),
            'pickup_deadline': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'pickup deadline (YYYY-MM-DD)'}),
            'contact_information': forms.TextInput(attrs={'class': 'form-control food-donate-form','placeholder':'contact information'}),



        }
        
        