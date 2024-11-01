from django import forms
from django.contrib.auth.models import User, Group
from .models import Volunteer

class VolunteerRegistrationForm(forms.ModelForm):
    # Add a role choice field
    ROLE_CHOICES = [('Admin', 'Admin'), ('Volunteer', 'Volunteer'), ('User', 'User')]
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'phone', 'skills', 'role']

