from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact_store(request):
    return render(request, "contact.html")


def contact_validation(request):
    form_email = request.POST['email']
    form_message = request.POST['message']

    Contact.objects.create(email=form_email, message=form_message)

    messages.success(request, "Your message saved successfully!")
    return redirect("contact_store")