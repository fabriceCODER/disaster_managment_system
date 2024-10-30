from django import forms
from .models import Volunteer

class VolunteerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'skills']
