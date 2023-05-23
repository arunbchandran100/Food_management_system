from django import forms
from .models import RequestDonation

class RequestDonationForm(forms.ModelForm):
    class Meta:
        model = RequestDonation
        fields = "__all__"
        labels = {
            'user': 'User',
            'count': 'Count',
            'description': 'Description',
            'request_date': 'Request Date',
            'location': 'Location',
            'deadline': 'Deadline',
            'contact_information': 'Contact Information',
        }
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Count'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'request_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Request Date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Deadline'}),
            'contact_information': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Information'}),
        }
