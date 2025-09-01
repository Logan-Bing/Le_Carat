from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .models import Customer
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            customer = form.save()
            first_name = request.POST.get("first_name")
            customer_mail = request.POST.get("email")
            subject = "Bienvenue dans notre Newsletter"
            message = f"Merci {first_name} d'avoir souscrit a la newsletter"
            if subject and message and customer_mail:
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL ,[ customer_mail ])
                except BadHeaderError:
                    return render("Invalid Header")
                return redirect('success', customer_id = customer.id)
    else:
        form = ContactForm()

    return render(request, "home.html", {'form': form})

def success_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, "sections/success.html", {"customer": customer})
