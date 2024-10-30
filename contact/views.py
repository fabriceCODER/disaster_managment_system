from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email logic
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    f"Contact Form Submission from {name}",
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                )
                return redirect('contact:success')
            except Exception as e:
                # Optionally log the error
                print(e)
                form.add_error(None, "There was an error sending your message. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def success(request):
    return render(request, 'contact/success.html')
