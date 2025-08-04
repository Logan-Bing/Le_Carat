from django import forms
from .models import Customer

class ContactForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone", "email"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
