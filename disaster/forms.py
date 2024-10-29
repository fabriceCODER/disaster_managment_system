# disaster/forms.py
from django import forms
from .models import Disaster
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from resourses.models import Resource

class DisasterForm(forms.ModelForm):
    resources_needed = forms.ModelMultipleChoiceField(
        queryset=Resource.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Disaster
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



