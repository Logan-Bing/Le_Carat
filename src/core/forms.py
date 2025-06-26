from django import forms
from .models import Customer

class ContactForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone", "email"]
