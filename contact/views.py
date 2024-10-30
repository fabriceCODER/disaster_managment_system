from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send an email notification
            subject = f"Contact Form Submission from {form.cleaned_data['name']}"
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = settings.EMAIL_HOST_USER  # Your email address
            recipient_list = ['your_recipient_email@example.com']  # Change to your desired recipient

            try:
                send_mail(subject, message, from_email, recipient_list)
                return redirect('contact_success')  # Redirect to a success page
            except Exception as e:
                # Handle error (log it, notify user, etc.)
                print(f"Error sending email: {e}")

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
