from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.post)
        if form.is_valid():
            form.save()  # crée et enregistre l'article
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {'form': form})
