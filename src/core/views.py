from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import ContactForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            customer = form.save()  # crée et enregistre l'article
            return redirect('success', customer_id = customer.id)
    else:
        form = ContactForm()

    return render(request, "home.html", {'form': form})

def success_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, "sections/success.html", {"customer": customer})
